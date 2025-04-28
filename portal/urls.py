from django.urls import path, include
from . import views as portal_views
from forum import views as forum_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portal'

urlpatterns = [
    path('', portal_views.HomeView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),

    # Forum
    path('forum', forum_views.home_forum, name='home_forum'),
    path('branch/<int:branch_id>/', forum_views.branch_detail, name='branch_detail'),
    path('comment/<int:comment_id>/like/', forum_views.like_comment, name='like_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)