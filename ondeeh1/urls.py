from django.urls import path

from . import views

urlpatterns = [
    path('api/paises/<str:pais>',views.api_pais),
]