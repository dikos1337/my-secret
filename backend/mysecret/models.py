from django.db import models


# Create your models here.
class Secret(models.Model):
    secret = models.TextField(max_length=8192)
    passphrase = models.CharField(max_length=64)
    lifetime = models.FloatField()
    created_date = models.DateTimeField("Дата создания")
    viewed = models.BooleanField(default=False)  # default False

    def __str__(self):
        return self.secret[:100] + ('...' if len(self.secret) > 100 else '')
