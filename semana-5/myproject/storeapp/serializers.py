from rest_framework.serializers import ModelSerializer
from .models import Product, Category

# importar ambas clases podemos crear nuestra clase serailizer
class ProductSerializer(ModelSerializer):
    class Meta:
        # paso 1 defiinis el modelo que usará este serializer
        model = Product
        #paso 2 definir son los campos que quiero usar el modelo
        # '__all__' es igual a decir que vamos a usar todos los campos del modelo
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

