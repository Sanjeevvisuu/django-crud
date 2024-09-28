from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",get,name="get"),
    path("api_get_specific/<int:id>/",get_specific,name="api_get_specific"),
    path("api_delete/<int:id>/",delete,name="delete"),
    path("api_update/<int:id>/",update,name="update"),
    path("create_api/",create_api,name="create_api"),
]