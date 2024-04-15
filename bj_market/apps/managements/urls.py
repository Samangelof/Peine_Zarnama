from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet, 
    CarProductView,
    CarProductDetailView,
    ApartmentProductView,
    ApartmentProductDetailView,
    GiftProductView,
    GiftProductDetailView,
    BeautyProductView,
    BeautyProductDetailView,
    SportProductView,
    SportProductDetailView,
    BookProductView,
    BookProductDetailView, 
    HouseholdProductView,
    HouseholdProductDetailView,
    ClothingProductView,
    ClothingProductDetailView,
    ElectronicProductView,
    ElectronicProductDetailView,
    ComplaintView,
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productimages', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('cars/', CarProductView.as_view(), name='car_product_list'),
    path('car/<int:pk>/', CarProductDetailView.as_view(), name='car_product_detail'),

    path('apartments/', ApartmentProductView.as_view(), name='apartment_product_list'),
    path('apartment/<int:pk>/', ApartmentProductDetailView.as_view(), name='apartment_product_detail'),

    path('gifts/', GiftProductView.as_view(), name='gift_product_list'),
    path('gift/<int:pk>/', GiftProductDetailView.as_view(), name='gift_product_detail'),

    path('beautys/', BeautyProductView.as_view(), name='beauty_product_list'),
    path('beauty/<int:pk>/', BeautyProductDetailView.as_view(), name='apartment_product_detail'),

    path('sports/', SportProductView.as_view(), name='beauty_product_list'),
    path('sport/<int:pk>/', SportProductDetailView.as_view(), name='apartment_product_detail'),



    path('books/', BookProductView.as_view(), name='book_product_list'),
    path('book/<int:pk>/', BookProductDetailView.as_view(), name='book_product_detail'),

    path('households/', HouseholdProductView.as_view(), name='household_product_list'),
    path('household/<int:pk>/', HouseholdProductDetailView.as_view(), name='household_product_detail'),

    path('clothings/', ClothingProductView.as_view(), name='clothing_product_list'),
    path('clothing/<int:pk>/', ClothingProductDetailView.as_view(), name='clothing_product_detail'),

    path('electronics/', ElectronicProductView.as_view(), name='electronic_product_list'),
    path('electronic/<int:pk>/', ElectronicProductDetailView.as_view(), name='electronic_product_detail'),



    path('complaints/', ComplaintView.as_view(), name='complaints'),
]
