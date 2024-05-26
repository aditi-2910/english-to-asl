from django.urls import path
from . import views

urlpatterns = [
    path("animation/", views.animationView, name="animation"),
    path("about/", views.about_view, name="about"),
    path("", views.home_view, name="home"),
]
