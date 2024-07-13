#impotar nuestra clase viewset
from .views import ProductViewSet, CategoryViewSet
# importar el router de DRF
from rest_framework.routers import DefaultRouter

#crear una instancia de defaultRouter
router = DefaultRouter()
#agregar una ruta usando router
router.register(r'products', ProductViewSet)
router.register(r'Categories', CategoryViewSet)

urlpatterns = router.urls
