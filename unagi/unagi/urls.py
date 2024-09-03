from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dash_admin/", admin.site.urls), # rewrite the admin URL to avoid bots
    path("", include("blog.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
