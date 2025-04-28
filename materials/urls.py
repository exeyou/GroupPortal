from django.urls import path
from materials import views

app_name = 'materials'

urlpatterns = [
    path('material_list', views.material_list, name='material_list'),
]