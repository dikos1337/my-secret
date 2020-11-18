import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone


# Create your models here.
class Secret(models.Model):
    """Модель для хранения секрета"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=True,
    )

    expiration_date = models.DateTimeField(
        verbose_name="Дата окончания срока действия")

    secret = models.TextField(verbose_name="Содержание секрета",
                              max_length=3000)

    passphrase = models.CharField(verbose_name="Фраза-пропуск",
                                  blank=True,
                                  max_length=64)

    lifetime = models.IntegerField(verbose_name="Время жизни секрета, секунд")

    preview_has_been_shown = models.BooleanField(
        verbose_name="Было ли показано превью для его создателя",
        default=False)

    def __str__(self):
        """Отображение в админке первые 100 символов секрета"""
        return self.secret[:100] + ("..." if len(self.secret) > 100 else "")

    def сheck_expiration_date(self):
        """Проверяет не истёк ли срок действия секрта, если истёк,
        то возвращает True иначе False
        """
        return self.expiration_date <= timezone.now()

    def save(self, *args, **kwargs):
        # Вычисляю дату окончания срока действия
        self.expiration_date = timezone.now() + timedelta(
            seconds=self.lifetime)

        super().save(*args, **kwargs)
