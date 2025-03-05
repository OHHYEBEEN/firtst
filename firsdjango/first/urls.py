from django.urls import path
from . import views
# . -> 현재 위치

urlpatterns = [
    
    path("", views.home, name='home'),
]