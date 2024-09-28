
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path("api/", include("rest_app.urls")),
    # if we use include method insted of name use namespace
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

]
