from django.urls import path
from . import views

app_name = "libgen"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("view/<int:pk>", views.view_book, name="view_book"),
]
