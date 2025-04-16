from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register_page/", views.register, name="register"),
    path("login_page/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]