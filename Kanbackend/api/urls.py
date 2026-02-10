from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrypoint),
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task),
]