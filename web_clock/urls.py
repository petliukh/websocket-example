from django.urls import path
from web_clock import views

urlpatterns = [
    path('', views.index, name='web-clock-live'),
]
