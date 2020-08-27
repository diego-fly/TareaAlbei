
from django.urls import path
from django.contrib import admin
from panaderia.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio)
]



