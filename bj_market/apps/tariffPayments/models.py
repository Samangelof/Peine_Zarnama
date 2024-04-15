from django.db import models


class TariffPlan(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тарифного плана")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    currency = models.CharField(max_length=3, verbose_name="Валюта")

    class Meta:
        verbose_name = "Тарифный план"
        verbose_name_plural = "Тарифные планы"

    def __str__(self):
        return self.name