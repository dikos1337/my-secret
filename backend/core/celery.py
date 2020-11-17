# from mysecret.models import Secret
# from datetime import datetime

# def delete_expired_secrets():
#     queryset = Secret.objects.filter(expiration_date__lte=datetime.now())
#     for secret in queryset:
#         secret.delete()

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
