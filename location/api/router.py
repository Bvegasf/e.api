from django.db import router
from rest_framework.routers import DefaultRouter
from location.api.views import CountryViewSet, CityViewSet
from rest_framework import urlpatterns

router = DefaultRouter()

router.register(r'country',CountryViewSet, basename='country')
router.register(r'city',CityViewSet,basename='City')

urlpatterns = router.urls