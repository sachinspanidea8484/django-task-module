from django.urls import path
from . import views

urlpatterns = [
    path('', views.firmware_category_list, name='firmware_category_list'),
]
