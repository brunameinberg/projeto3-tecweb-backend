from django.urls import path

from . import views

urlpatterns = [
    path('api/token',views.api_get_token),
    path('api/users/', views.api_user),
    path('api/pontuacao/', views.api_pontuacao),
]