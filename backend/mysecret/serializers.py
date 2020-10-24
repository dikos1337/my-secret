from .models import Secret
from rest_framework import serializers


class RetrieveSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = "__all__"


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'secret', 'passphrase', 'lifetime')
