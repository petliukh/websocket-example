from django.urls import path
from live_calculator import views

urlpatterns = [
    path('', views.index, name='live-calculator'),
]
