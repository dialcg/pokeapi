from rest_framework import serializers
from core.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """Serialize Pokemon info to expose records to the API."""
    
    class Meta:
        model = Pokemon
        fields = '__all__'