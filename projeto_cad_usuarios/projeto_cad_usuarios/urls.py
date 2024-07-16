from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referencia
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("usuarios/", views.usuarios, name="listagem_usuarios"),
]
