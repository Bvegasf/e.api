from django.urls import path
from location.api.views import ContinentalRegionListCreatedAPIView, ContinentalRegionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('continental-region/create/',ContinentalRegionListCreatedAPIView.as_view(), name='continenatal'),
    path('continental-region/detail/', ContinentalRegionRetrieveUpdateDestroyAPIView.as_view(), name= 'continental update'),
    
]