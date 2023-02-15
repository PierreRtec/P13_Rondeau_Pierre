from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("oc_lettings_site.lettings.urls"), name="lettings"),
    path("profiles/", include("oc_lettings_site.profiles.urls"), name="profiles"),
    path("admin/", admin.site.urls),
]
