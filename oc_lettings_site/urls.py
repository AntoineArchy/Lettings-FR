from django.contrib import admin
from django.urls import path

import oc_lettings_site.lettings.views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Location List/Select
    path("lettings/", oc_lettings_site.lettings.views.lettings_index, name="lettings_index"),
    path("lettings/<str:letting_id>/", oc_lettings_site.lettings.views.letting, name="letting"),
    # Profile List/Select
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
    # Administration
    path("admin/", admin.site.urls),
]
