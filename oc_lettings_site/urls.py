from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Location List/Select
    path("lettings/", include("oc_lettings_site.lettings.urls")),
    # Profile List/Select
    path("profiles/", include("oc_lettings_site.profiles.urls")),
    # Administration
    path("admin/", admin.site.urls),
]
