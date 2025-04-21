from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'gallery'
urlpatterns = [
    path('', views.media_gallery, name='media_gallery'),
    path('upload/', views.upload_media, name='upload_media'),
    path('moderate/', views.moderate_media, name='moderate_media'),
    path('approve/<int:media_id>/', views.approve_media, name='approve_media'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
