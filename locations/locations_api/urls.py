from django.urls import path
from . import views

urlpatterns = [
    path('api/locations', views.LocationList.as_view(), name='location_list'), 
    path('api/locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
]