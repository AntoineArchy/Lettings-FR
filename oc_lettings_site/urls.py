from django.contrib import admin
from django.urls import path

import oc_lettings_site.lettings.views
import oc_lettings_site.profiles.views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Location List/Select
    path("lettings/", oc_lettings_site.lettings.views.index, name="lettings_index"),
    path("lettings/<str:letting_id>/", oc_lettings_site.lettings.views.letting, name="letting"),
    # Profile List/Select
    path("profiles/", oc_lettings_site.profiles.views.index, name="profiles_index"),
    path("profiles/<str:username>/", oc_lettings_site.profiles.views.profile, name="profile"),
    # Administration
    path("admin/", admin.site.urls),
]
