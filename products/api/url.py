from django.urls import path
from products.api.views.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProductListAPIView
from products.api.views.products_view import ProductsListAPIView,ProductCreatedAPIView,ProductsDeleteAPIView, ProductsUpdateAPIView,ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('meausure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name='Indicator'),
    path('category/',CategoryProductListAPIView.as_view(), name='measure_unit'),
    path('products/list/',ProductsListAPIView.as_view(), name='products'),
    path('products/create/',ProductCreatedAPIView.as_view(), name='products'),
    path('products/detailupdatedelete/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(),name='products'),
    path('products/delete/<int:pk>',ProductsDeleteAPIView.as_view(),name='products_delete'),
    path('products/update/<int:pk>',ProductsUpdateAPIView.as_view(),name='Products_update')
    ]
