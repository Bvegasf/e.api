# al realizar la definicion de un router se importa DefaultRouter desde la libreiria
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
#se importa el Viewset que se usara
from products.api.views.products_view import ProductViewset

# se define el router
router= DefaultRouter()
# Ve realiza el registro del router, con r'' se define la url y se llama al viewset

router.register(r'products',ProductViewset, basename = 'products')

urlpatterns = router.urls


