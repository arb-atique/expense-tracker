from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create_expense, name='create'),
    path('edit/<int:pk>/', views.edit_expense, name='edit'),
    path('delete/<int:pk>/', views.delete_expense, name='delete'),
]
