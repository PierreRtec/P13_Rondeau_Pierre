from django.contrib import admin
from django.urls import include, path

from . import views


# this code is for sentry testing
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("oc_lettings_site.lettings.urls"), name="lettings"),
    path("profiles/", include("oc_lettings_site.profiles.urls"), name="profiles"),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
