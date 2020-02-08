
from django.contrib import admin
from django.urls import path
from core.views import subirImagen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subir-imagen', subirImagen)
]
