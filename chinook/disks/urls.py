from django.urls import path
from . import views

app_name = "disks"
urlpatterns = [
    path("", views.album_list, name="album list"),
    path("<int:album_id>", views.album_detail, name="album detail"),
]