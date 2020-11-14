from rest_framework import generics, status, views
from rest_framework.response import Response

from .models import Secret
from .serializers import CheckAvailableSerializer, SecretSerializer

# Create your views here.


class CreateSecretView(generics.CreateAPIView):
    """Создание секрета"""

    queryset = Secret.objects.all()
    serializer_class = SecretSerializer


class CheckAvailableView(generics.RetrieveAPIView):
    """View для проверка фронтом есть ли у секрета пароль чтобы решить
    рендерить или нет форму для пароля"""
    queryset = Secret.objects.all()
    serializer_class = CheckAvailableSerializer
    # TODO если сущетвует пароль то поле с паролем
    # заменить на True, а не отправлять сам пароль
    # если щуствует if тогда флаг Available тоже true иначе false


# class RetriveSecretView(generics.RetrieveAPIView, generics.DestroyAPIView):
#     queryset = Secret.objects.all()
#     serializer_class = SecretSerializer
class RetriveSecretView(views.APIView):
    """Получение секрета с проверкой правильности пароля"""
    def post(self, request, pk):
        # TODO сделать проверку, обернуть в Exception или что то тако
        secrets = Secret.objects.get(pk=pk)
        serializer = SecretSerializer(secrets, many=False)

        # Сверяю пароль из формы с паролем секрета
        secret_passphrase = request.data.get("passphrase", "")
        if secret_passphrase != serializer.data["passphrase"]:
            return Response({"error": "passphrase is invalid"},
                            status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        _ = self
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO проверять если метод пост то проверять пароль
    # а потом отдавать данные если гет то просто отдавать
    # А может быть всегда принимать гет чтоб всегда сверять пароль
    # а то можно будет заменить пост на гет и без пароля узнать секрет?


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
