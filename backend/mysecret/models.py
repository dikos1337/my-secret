from django.db import models


# Create your models here.
class Secret(models.Model):
    created_date = models.DateTimeField(verbose_name="Дата создания",
                                        auto_now=True)
    secret = models.TextField(verbose_name="Содержание секрета",
                              max_length=8192)
    passphrase = models.CharField(verbose_name="Фраза-пропуск", max_length=64)
    lifetime = models.FloatField(
        verbose_name="Lifetime, время жизни секрета", )
    viewed = models.BooleanField(verbose_name="Просмотрел ли секрет",
                                 default=False)  # default False

    def __str__(self):
        return self.secret[:100] + ("..." if len(self.secret) > 100 else "")
