from django.contrib import admin
from django.urls import path, include
from reviews.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("", include("reviews.urls")),
]