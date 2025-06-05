from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('categories/', views.task_category_list, name='task_category_list'),
]
