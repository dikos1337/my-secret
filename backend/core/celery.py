from mysecret.models import Secret
from datetime import datetime


def delete_expired_secrets():
    queryset = Secret.objects.filter(expiration_date__lte=datetime.now())
    for secret in queryset:
        secret.delete()
