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
from django.urls import path,include
from rest_framework import permissions
from users.views import Login,Logout,UserToken




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
    path('city/', include('location.api.router'))
    ]
