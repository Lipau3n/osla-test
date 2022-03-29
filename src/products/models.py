from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Имя товара", max_length=128)
    price = models.CharField(verbose_name="Цена товара за единицу в руб.", max_length=128)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Work(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.FloatField(verbose_name="Кол-во использованного товара", null=True, blank=False)
    date = models.DateTimeField(verbose_name="Дата выполнения работы")

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
