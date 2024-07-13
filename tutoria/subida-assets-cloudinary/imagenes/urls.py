from django.urls import path
from .views import SubidaImagen

urlpatterns = [
    path('subida/', SubidaImagen.as_view(), name) #iempre que es por es necesario /
]