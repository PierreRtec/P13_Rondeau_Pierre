from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views


# this code is for sentry testing
def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls"), name="lettings"),
    path("profiles/", include("profiles.urls"), name="profiles"),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
