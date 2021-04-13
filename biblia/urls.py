from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('detalhes/<slug:slug>', views.Detalhes.as_view(), name='detalhes'),
    path('search/', views.Search.as_view(), name="search"),
]
