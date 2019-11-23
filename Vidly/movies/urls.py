from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.index, name="hello")
    path('welcome', views.welcome, name="welcome"),
    path("aboutMe", views.about, name="about")
]