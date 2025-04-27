from django.urls import path
from forum import views as forum_views

app_name = 'forum'

urlpatterns = [
    path('forum', forum_views.home_forum, name='home_forum'),
    path('branch/<int:branch_id>/', forum_views.branch_detail, name='branch_detail'),
    path('comment/<int:comment_id>/like/', forum_views.like_comment, name='like_comment'),
    path('comment/delete/<int:comment_id>/', forum_views.delete_comment, name='delete_comment'),
]
