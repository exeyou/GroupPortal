from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register_page/", views.register, name="register"),
    path("login_page/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("portfolio/", views.my_portfolio, name="my_portfolio"),
    path("portfolio/add/", views.add_project, name="add_project"),
    path("portfolio/edit/<int:pk>/", views.edit_project, name="edit_project"),
    path("portfolio/delete/<int:pk>/", views.delete_project, name="delete_project"),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
