from core.celery import app
from django.utils import timezone

from mysecret.models import Secret


@app.task
def delete_expired_secrets():
    queryset = Secret.objects.filter(expiration_date__lte=timezone.now())
    queryset.delete()
    return True
