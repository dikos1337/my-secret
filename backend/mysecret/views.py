from rest_framework import generics, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Secret
from .serializers import (CheckAvailableSerializer, PrivateSerializer,
                          SecretSerializer)


class CreateSecretView(generics.CreateAPIView):
    """Создание секрета"""
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer


class CheckAvailableView(generics.RetrieveAPIView):
    """View для проверка фронтом есть ли у секрета пароль чтобы решить
    рендерить или нет форму для пароля"""
    serializer_class = CheckAvailableSerializer

    def retrieve(self, request, pk, **kwargs):
        instance = get_object_or_404(Secret, pk=pk)
        serializer = self.get_serializer(instance)

        # Возвращаю флаг вместо пароля
        serializer._data["passphrase"] = self._decide_passphrase_flag(
            serializer)
        return Response(serializer.data)

    def _decide_passphrase_flag(self, serializer):
        """Решаю какой флаг вернуть, если пароль нужен, то True
        иначе False, от этого зависит рендерить ли форму на фронте.
        """
        return True if serializer.data["passphrase"] else False


class RetriveSecretView(views.APIView):
    """Получение секрета с проверкой правильности пароля"""
    def post(self, request, pk):
        secret = get_object_or_404(Secret, pk=pk)
        serializer = SecretSerializer(secret, many=False)

        # Сверяю пароль из формы с паролем секрета
        if self._validate_passphrase(request, serializer):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "passphrase is invalid"},
                            status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk, format=None):
        secret = get_object_or_404(Secret, pk=pk)
        serializer = SecretSerializer(secret, many=False)

        if self._validate_passphrase(request, serializer):
            secret.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "passphrase is invalid"},
                            status=status.HTTP_403_FORBIDDEN)

    def _validate_passphrase(self, request, serializer):
        """Возвращает результат проверки пароля из формы с паролем секрета"""
        passphrase = request.data.get("passphrase", "")
        if passphrase != serializer.data["passphrase"]:
            return False
        else:
            return True


class PrivateView(views.APIView):
    def get(self, request, pk):
        secret = get_object_or_404(Secret, pk=pk)
        serializer = PrivateSerializer(secret, many=False)

        # на /private/ надо показать секрет только 1 раз, для его создателя
        # После надо показывать звездочки
        if secret.preview_has_been_shown is False:
            secret.preview_has_been_shown = True
            secret.save()
        else:
            secret.secret = "*" * 10

        return Response(serializer.data)


# class TestView(views.APIView):
#     def get(self, request):
#         secrets = Secret.objects.all()

#         # the many param informs the serializer
#         # that it will be serializing more than a single article.
#         serializer = CreateSecretSerializer(secrets, many=True)
#         return Response({"secrets": serializer.data})

#     def post(self, request):
#         secret = request.data.get('secret')
#         # Create an article from the above data
#         serializer = CreateSecretSerializer(data=secret)
#         if serializer.is_valid(raise_exception=True):
#             # secret_saved =
#             serializer.save()
#         return Response({
#             "success": "Secret created successfully",
#             "data": serializer.data  # .get('uuid'),
#         })
