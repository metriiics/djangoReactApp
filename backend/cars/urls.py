from django.urls import path, re_path
from .views import CarsApiView, CarDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/cars/', CarsApiView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]