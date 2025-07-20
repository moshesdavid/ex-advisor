from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from reviews.views import home, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", logout_view, name="logout")
]