from django.contrib import admin
from django.urls import path

from abilitymanager import views


urlpatterns = [
    path('', views.PokemonListView.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(), name='pokemon-detail'),
    path('pokemon/<int:pk>/ability/', views.AbilityCreateView.as_view(), name='ability-create'),
    path('ability/<int:pk>/', views.AbilityUpdateView.as_view(), name='ability-update'),
    path('ability/<int:pk>/delete/', views.AbilityDeleteView.as_view(), name='ability-delete'),
]
