from mysecret.models import Secret
from datetime import datetime

from core.celery import app


@app.task
def delete_expired_secrets():
    queryset = Secret.objects.filter(expiration_date__lte=datetime.now())
    queryset.delete()
    return True
