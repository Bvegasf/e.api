from django.urls import path
from users.API.api import user_api_view,user_detail_view

urlpatterns = [
    path('usuario/', user_api_view, name='Usuario_api'),
    path('usuario/<int:pk>', user_detail_view, name='usuario_detail_view')
]
