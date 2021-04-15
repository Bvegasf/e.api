from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns
from empleado.api.view import *


router = DefaultRouter()


router.register(r'department', DepartmentViewSet, basename = 'department')
router.register(r'job', JobViewSet, basename = 'Job')


urlpatterns = router.urls