from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'grades'

urlpatterns = [
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.add_grade, name='add_grade'),
    path('grades/edit/<int:pk>/', views.edit_grade, name='edit_grade'),
    path('grades/delete/<int:pk>/', views.delete_grade, name='delete_grade'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
