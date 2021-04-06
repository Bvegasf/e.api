from django.db import router
from rest_framework.routers import DefaultRouter
from location.api.views import CountryModelViewset, CityModelViewset
from rest_framework import urlpatterns

router = DefaultRouter()

router.register(r'country',CountryModelViewset, basename='country')
router.register(r'city',CityModelViewset,basename='City')

urlpatterns = router.urls