from collections import defaultdict
from rest_framework.routers import DefaultRouter
from rest_framework import urlpatterns
from branch.api.view import BranchModelViewset


router = DefaultRouter()


router.register(r'branch', BranchModelViewset, basename= 'branch')

urlpatterns=router.urls
