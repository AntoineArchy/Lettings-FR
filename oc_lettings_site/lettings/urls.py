from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<str:letting_id>/", views.letting, name="letting"),
]
