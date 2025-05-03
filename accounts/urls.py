from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.add_grade, name='add_grade'),
    path('grades/edit/<int:pk>/', views.edit_grade, name='edit_grade'),
    path('grades/delete/<int:pk>/', views.delete_grade, name='delete_grade'),
]