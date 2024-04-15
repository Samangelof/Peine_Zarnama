from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductImage,
    CarProduct,
    ApartmentProduct,
    GiftProduct,
    BeautyProduct,
    SportProduct,
    BookProduct,
    HouseholdProduct,
    ClothingProduct,
    ElectronicsProduct,
    Complaint
)

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'category',
            'description',
            'location',
            'price',
            'image',
            'owner'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CarProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = CarProduct
        fields = BaseProductSerializer.Meta.fields + [
            'car_make',
            'car_model',
            'car_year'
        ]


class ApartmentProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ApartmentProduct
        fields = BaseProductSerializer.Meta.fields + [
            'sale_type',
            'apartment_area',
            'apartment_rooms'
        ]


class GiftProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = GiftProduct
        fields = BaseProductSerializer.Meta.fields + [
            'occasion',
            'recipient',
            'gift_wrapping',
        ]


class BeautyProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = BeautyProduct
        fields = BaseProductSerializer.Meta.fields + [
            'skin_type',
            'hair_type',
            'benefits',
        ]


class SportProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = SportProduct
        fields = BaseProductSerializer.Meta.fields + [
            'sport_type',
            'activity',
            'duration',
        ]


class BookProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = BookProduct
        fields = BaseProductSerializer.Meta.fields + [
            'author',
            'genre',
            'count_pages',
            'book_year'
        ]


class HouseholdProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = HouseholdProduct
        fields = BaseProductSerializer.Meta.fields + [
            'usage',
            'ingredients',
            'safety_instructions',
        ]


class ClothingProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ClothingProduct
        fields = BaseProductSerializer.Meta.fields + [
            'size',
            'color',
            'material',
        ]


class ElectronicProductSerializer(serializers.ModelSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ElectronicsProduct
        fields = BaseProductSerializer.Meta.fields + [
            'brand',
            'model_name',
            'specs',
        ]







# Жалоба
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'