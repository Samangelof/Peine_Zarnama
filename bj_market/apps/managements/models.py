from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from auths.models import CustomUser


def validate_video_file_size(value):
    filesize = value.size
    if filesize > 50 * 1024 * 1024:  # 50 MB
        raise ValidationError(_('The maximum file size that can be uploaded is 50MB'))


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='images_product')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображениие')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    video = models.FileField(upload_to='product_videos', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov']), 
        validate_video_file_size
        ], verbose_name='Видео', blank=True, null=True)
    location = models.CharField(max_length=255, verbose_name='Местоположение')
    social_media = models.URLField(max_length=255, blank=True, verbose_name="Ссылка на социальные сети")
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')

    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('inactive', 'Неактивный'),
        ('deleted', 'Удаленный'),
    ]
    status = models.CharField(max_length=10, verbose_name='Статус', choices=STATUS_CHOICES, default='inactive')
    created_at = models.DateTimeField(auto_now_add=True)

    tariff_paid = models.BooleanField(default=False, verbose_name='Подтвержденный платеж')
    
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CarProduct(Product):
    car_make = models.CharField(max_length=100, verbose_name='Марка автомобиля', blank=True, null=True)
    car_model = models.CharField(max_length=100, verbose_name='Модель автомобиля', blank=True, null=True)
    car_year = models.IntegerField(verbose_name='Год выпуска автомобиля', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class ApartmentProduct(Product):
    apartment_area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Площадь квартиры', blank=False, null=False)
    apartment_rooms = models.IntegerField(verbose_name='Количество комнат в квартире', blank=False, null=False)

    SALE_TYPE_CHOICES = [
        ('day', 'Сутки'),
        ('rent', 'Аренда'),
        ('sale', 'Продажа'),
    ]
    sale_type = models.CharField(max_length=10, choices=SALE_TYPE_CHOICES, verbose_name='Тип предложения', default='sale')

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class GiftProduct(Product):
    occasion = models.CharField(max_length=100, verbose_name='Повод', blank=False, null=False)
    recipient = models.CharField(max_length=100, verbose_name='Получатель', blank=False, null=False)
    gift_wrapping = models.BooleanField(default=False, verbose_name='Упаковка подарка', blank=False, null=False)

    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'


class BeautyProduct(Product):
    skin_type = models.CharField(max_length=50, verbose_name='Тип кожи', blank=False, null=False)
    hair_type = models.CharField(max_length=50, verbose_name='Тип волос', blank=False, null=False)
    benefits = models.TextField(verbose_name='Полезные свойства', blank=False, null=False)

    class Meta:
        verbose_name = 'Товар для здоровья и красоты'
        verbose_name_plural = 'Товары для здоровья и красоты'


class SportProduct(Product):
    sport_type = models.CharField(max_length=50, verbose_name='Вид спорта', blank=False, null=False)
    activity = models.CharField(max_length=100, verbose_name='Вид деятельности', blank=False, null=False)
    duration = models.DurationField(verbose_name='Продолжительность', blank=False, null=False)

    class Meta:
        verbose_name = 'Товар для спорта и отдыха'
        verbose_name_plural = 'Товары для спорта и отдыха'


class BookProduct(Product):
    author = models.CharField(max_length=100, verbose_name='Автор', blank=False, null=False)
    genre = models.CharField(max_length=50, verbose_name='Жанр', blank=False, null=False)
    count_pages = models.IntegerField(verbose_name='Количество страниц', blank=False, null=False)
    book_year = models.CharField(max_length=4,verbose_name='Год выпуска', blank=False, null=False)

    class Meta:
        verbose_name = 'Книга или учебник'
        verbose_name_plural = 'Книги и учебники'


class HouseholdProduct(Product):
    usage = models.TextField(verbose_name='Способ применения', blank=False, null=False)
    ingredients = models.TextField(verbose_name='Состав', blank=False, null=False)
    safety_instructions = models.TextField(verbose_name='Инструкции по безопасности', blank=False, null=False)

    class Meta:
        verbose_name = 'Товар для дома и бытовой химии'
        verbose_name_plural = 'Товары для дома и бытовой химии'


class ClothingProduct(Product):
    size = models.CharField(max_length=20, verbose_name='Размер', blank=False, null=False)
    color = models.CharField(max_length=50, verbose_name='Цвет', blank=False, null=False)
    material = models.CharField(max_length=100, verbose_name='Материал', blank=False, null=False)

    class Meta:
        verbose_name = 'Одежда или обувь'
        verbose_name_plural = 'Одежда и обувь'


class ElectronicsProduct(Product):
    brand = models.CharField(max_length=100, verbose_name='Бренд', blank=False, null=False)
    model_name = models.CharField(max_length=100, verbose_name='Модель', blank=False, null=False)
    specs = models.TextField(verbose_name='Характеристики', blank=False, null=False)

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'




class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'