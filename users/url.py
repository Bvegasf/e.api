from django.urls import path
from users.API.api import UserAPIView

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name='Usuario_api')
]
