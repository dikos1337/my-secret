from hashlib import sha256

from rest_framework import generics, status, views
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from mysecret.models import Secret
from mysecret.serializers import (CheckAvailableSerializer, PrivateSerializer,
                                  SecretSerializer)


class CreateSecretView(generics.CreateAPIView):
    """Создание секрета"""
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer

    def create(self, request, *args, **kwargs):
        passphrase = request.data.get('passphrase', '')

        # Если пароль есть то записываю его хеш иначе оставляю пустую строку
        if passphrase:
            passphrase_bytes_string = passphrase.encode()
            passphrase_hash = sha256(passphrase_bytes_string).hexdigest()
            request.data['passphrase'] = passphrase_hash

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class CheckAvailableView(generics.RetrieveAPIView):
    """View для проверка фронтом есть ли у секрета пароль чтобы решить
    рендерить или нет форму для пароля
    """
    serializer_class = CheckAvailableSerializer

    def retrieve(self, request, pk, **kwargs):
        instance = get_object_or_404(Secret, pk=pk)
        if instance.сheck_expiration_date():
            instance.delete()
            raise NotFound

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
        if secret.сheck_expiration_date():
            secret.delete()
            raise NotFound

        serializer = SecretSerializer(secret, many=False)

        # Сверяю пароль из формы с паролем секрета
        if self._validate_passphrase(request, serializer):
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied(detail="passphrase is invalid")

    def delete(self, request, pk, format=None):
        secret = get_object_or_404(Secret, pk=pk)
        serializer = SecretSerializer(secret, many=False)

        if self._validate_passphrase(request, serializer):
            secret.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied(detail="passphrase is invalid")

    def _validate_passphrase(self, request, serializer):
        """Возвращает результат проверки пароля из формы с паролем секрета,
        если пароли совпдают то возвращает True иначе False
        """
        passphrase = request.data.get("passphrase", "")

        # Если пароль не пустой то вычисляю хеш и сравниваю его
        if passphrase:
            passphrase_bytes_string = passphrase.encode()
            passphrase_hash = sha256(passphrase_bytes_string).hexdigest()

            return passphrase_hash == serializer.data["passphrase"]

        # Иначе сравниваю пустую строчку с пустой строчкой
        else:
            return passphrase == serializer.data["passphrase"]


class PrivateView(views.APIView):
    def get(self, request, pk):
        secret = get_object_or_404(Secret, pk=pk)
        if secret.сheck_expiration_date():
            secret.delete()
            raise NotFound

        serializer = PrivateSerializer(secret, many=False)

        # на /private/ надо показать секрет только 1 раз, для его создателя
        # После надо показывать звездочки
        if secret.preview_has_been_shown is False:
            secret.preview_has_been_shown = True
            secret.save()
        else:
            secret.secret = "*" * 10

        return Response(serializer.data)
