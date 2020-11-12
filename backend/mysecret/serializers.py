from rest_framework import serializers

from .models import Secret


class CheckAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'passphrase')


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'secret', 'passphrase', 'lifetime')
