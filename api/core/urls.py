from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .api import PokemonListCreateAPIView


urlpatterns = [
    path('', PokemonListCreateAPIView.as_view(), name='api-pokemon-list-create'),
]
