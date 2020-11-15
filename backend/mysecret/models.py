import uuid

from django.db import models


# Create your models here.
class Secret(models.Model):
    """Модель для хранения секрета"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=True,
    )

    secret = models.TextField(verbose_name="Содержание секрета",
                              max_length=3000)

    passphrase = models.CharField(verbose_name="Фраза-пропуск",
                                  blank=True,
                                  max_length=64)

    lifetime = models.FloatField(verbose_name="Lifetime, время жизни секрета")

    preview_has_been_shown = models.BooleanField(
        verbose_name="Было ли показано превью для его создателя",
        default=False)

    def __str__(self):
        """Отображение в админке первые 100 символов секрета"""
        return self.secret[:100] + ("..." if len(self.secret) > 100 else "")
