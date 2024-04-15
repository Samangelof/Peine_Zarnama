from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
from .permissions import IsOwnerOrReadOnly
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
    ElectronicsProduct
)
from .serializers import (
    BaseProductSerializer,
    CategorySerializer,
    ProductImageSerializer,
    CarProductSerializer,
    ApartmentProductSerializer,
    GiftProductSerializer,
    BeautyProductSerializer,
    SportProductSerializer,
    BookProductSerializer,
    HouseholdProductSerializer,
    ClothingProductSerializer,
    ElectronicProductSerializer,

    ComplaintSerializer
)


#
# (GET, POST, PUT/PATCH, DELETE)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Object deleted successfully'}, status=HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BaseProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'location', 'additional_info']
    filterset_fields = ['location']

    def get_queryset(self):
        queryset = super().get_queryset()
        city = self.request.query_params.get('location')
        if city:
            queryset = queryset.filter(location=city)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Object deleted successfully'}, status=HTTP_204_NO_CONTENT)
    

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]
#       
    

    
CATEGORIES = [
    'apartments',
    'houses', 'cars',
    'books', 'electronics',
    'clotching', 'sports',
    'Households', 'beautys'
]

# Car
class CarProductView(ListCreateAPIView):
    queryset = CarProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = CarProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class CarProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = CarProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Apartament
class ApartmentProductView(ListCreateAPIView):
    queryset = ApartmentProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ApartmentProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class ApartmentProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ApartmentProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Gift
class GiftProductView(ListCreateAPIView):
    queryset = GiftProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = GiftProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class GiftProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = GiftProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = GiftProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Beauty
class BeautyProductView(ListCreateAPIView):
    queryset = BeautyProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = BookProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class BeautyProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BeautyProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = BookProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Beauty
class SportProductView(ListCreateAPIView):
    queryset = SportProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = SportProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class SportProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SportProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = SportProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Book
class BookProductView(ListCreateAPIView):
    queryset = BookProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = BookProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class BookProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BookProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = BookProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Household
class HouseholdProductView(ListCreateAPIView):
    queryset = HouseholdProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = HouseholdProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class HouseholdProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HouseholdProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = HouseholdProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Clothing
class ClothingProductView(ListCreateAPIView):
    queryset = ClothingProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ClothingProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class ClothingProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ClothingProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ClothingProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


# Electronic
class ElectronicProductView(ListCreateAPIView):
    queryset = ElectronicsProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ElectronicProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class ElectronicProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ElectronicsProduct.objects.filter(category__name__in=CATEGORIES)
    serializer_class = ElectronicProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


#  Жалоба
class ComplaintView(APIView):
    def post(self, request):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)