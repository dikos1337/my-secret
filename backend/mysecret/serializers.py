from rest_framework import serializers

from mysecret.models import Secret


class CheckAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'passphrase')


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'secret', 'passphrase', 'lifetime')


class PrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'lifetime', 'created_date', 'secret')
