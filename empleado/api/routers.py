from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns
from empleado.api.view import *


router = DefaultRouter()


router.register(r'department', DepartmentViewset, basename = 'department')
router.register(r'job', JobViewset, basename = 'Job')


urlpatterns = router.urls