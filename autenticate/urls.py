from django.urls import path
from . import views

urlpatterns = [
    path('usuarios', views.user_list, name = "usuarios"),
    path('cadastro', views.add_user, name = "cadastro"),
]