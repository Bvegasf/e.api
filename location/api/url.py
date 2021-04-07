from django.urls import path
from location.api.views import ContinentalRegionListCreatedAPIView, ContinentalRegionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('continental/create/',ContinentalRegionListCreatedAPIView.as_view(), name='continenatal'),
    path('continental/detail/<int:pk>', ContinentalRegionRetrieveUpdateDestroyAPIView.as_view(), name= 'continental update'),
    
]