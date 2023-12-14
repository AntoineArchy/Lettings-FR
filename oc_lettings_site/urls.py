from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = "oc_lettings_site.views.oc_lettings_site_404"
handler400 = "oc_lettings_site.views.oc_lettings_site_400"
handler500 = "oc_lettings_site.views.oc_lettings_site_500"

urlpatterns = [
    path("", views.index, name="index"),
    # Location List/Select
    path("lettings/", include("oc_lettings_site.lettings.urls")),
    # Profile List/Select
    path("profiles/", include("oc_lettings_site.profiles.urls")),
    # Administration
    path("admin/", admin.site.urls),
]
