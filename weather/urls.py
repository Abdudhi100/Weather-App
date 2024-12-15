from django.contrib import admin
from django.urls import path
from .views import weather_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', weather_view, name= 'weather_view'),
]