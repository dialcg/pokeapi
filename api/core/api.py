from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Pokemon
from core.services import PokemonService

from .serializers import PokemonSerializer


class PokemonListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating Pokemon.

    This view allows authenticated users to list Pokemon and create new Pokemon entries.

    Attributes:
        serializer_class (serializers.Serializer): The serializer class used for Pokemon objects.
        authentication_classes (list): The authentication classes required for this view.
        permission_classes (list): The permission classes required for this view.

    Methods:
        get_queryset(self): Get the queryset of Pokemon from the service and filters the queryset
        if 'q' param is present in the URL.
        perform_create(self, serializer): Create a new Pokemon using the service.

    """
    serializer_class = PokemonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> list[Pokemon]:
        """
        Get the queryset of Pokemon using the service.

        Returns:
            queryset: A queryset containing all Pokemon objects.
        """

        queryset = PokemonService().get_all_pokemons()

        search_param = self.request.query_params.get('q', None)

        if search_param:
            queryset = queryset.filter(name__icontains=search_param)  

        return queryset

    def perform_create(self, serializer) -> Pokemon:
        """
        Create a new Pokemon using the service.

        Args:
            serializer (serializers.Serializer): The validated data for the new Pokemon.

        Returns:
            None
        """

        PokemonService().create_pokemon(serializer.validated_data['name'])
