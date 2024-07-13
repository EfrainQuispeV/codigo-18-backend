from .models import Product, Category #model
from .serializers import ProductSerializer, CategorySerializer # serializer
from rest_framework.viewsets import ModelViewSet # la clase de rest gramework que permite crear n CRUD

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer