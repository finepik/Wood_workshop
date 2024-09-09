from django.db import models


class Category(models.Model):
    """
    Модель Category представляет категорию изделия

    """

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self) -> str:
        return self.name


def product_preview_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Product(models.Model):
    """
    Модель Product представляет товар, который можно продавать в интернет-магазине

    """

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"

    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    description = models.TextField(null=False, blank=True, verbose_name='Описание', db_index=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.SmallIntegerField(default=0, verbose_name='Скидка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    favorite = models.BooleanField(default=False, verbose_name='Избранное')
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path,
                                verbose_name='Основное фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products',
                                 verbose_name='Категория')

    def __str__(self) -> str:
        return self.name


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "product/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    """
       Модель ProductImage представляет товар, который можно продавать в интернет-магазине

    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_images_directory_path, verbose_name='Фото')
    description = models.CharField(max_length=200, null=False, blank=True, verbose_name='Заметки к фото')


class Proposal(models.Model):
    """
    Модель Proposal представляет заявки пользователей за консультацией

    """

    class Meta:
        verbose_name = "Заявкa"
        verbose_name_plural = "Заявки"

    customer_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    description = models.TextField(null=False, blank=True, verbose_name='Пожелания')

    def __str__(self) -> str:
        return ""
