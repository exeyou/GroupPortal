from django.urls import path
from . import views as portal_views
from forum import views as forum_views

app_name = 'portal'

urlpatterns = [
    path('', portal_views.HomeView.as_view(), name='home'),

    # Forum
    path('forum', forum_views.home_forum, name='home_forum'),
    path('branch/<int:branch_id>/', forum_views.branch_detail, name='branch_detail'),
    path('comment/<int:comment_id>/like/', forum_views.like_comment, name='like_comment'),
]
