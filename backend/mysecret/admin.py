from django.contrib import admin

# Register your models here.
from mysecret.models import Secret

admin.site.register(Secret)
