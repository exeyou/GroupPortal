from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),
    path('create/', views.create_announcement, name='create_announcement'),
    path('edit/<int:pk>/', views.edit_announcement, name='edit_announcement'),
    path('delete/<int:pk>/', views.delete_announcement, name='delete_announcement'),
]

