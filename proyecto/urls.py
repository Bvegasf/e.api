"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
from users.views import Login,Logout,UserToken
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion base de la API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="brayanjovegas@gmail.com"),
      license=openapi.License(name="BD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',include('users.API.url') ),
    path('products/',include('products.api.routers')),
    path('',Login.as_view(), name= 'login'),
    path('logout/',Logout.as_view(), name='Logout'),
    path('employee/', include('empleado.api.url')),
    path('department/', include('empleado.api.routers')),
    path('job/', include('empleado.api.routers')),
    path('refresh-token/',UserToken.as_view(), name= 'refresh token'),
    path('location/',include('location.api.url'), name='locacion'),
    path('country/', include('location.api.router')),
    path('city/', include('location.api.router')),
    path('branch', include('branch.api.router')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path(r'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
