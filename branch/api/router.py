from collections import defaultdict
from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns
from branch.api.view import BranchViewSet


router = DefaultRouter()


router.register(r'branch', BranchViewSet, basename= 'branch')

urlpatterns=router.urls
