from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from core.models import (
    Pokemon,
    PokemonAbility
)
from core.services import (
    PokemonService,
    PokemonAbilityService
)


class PokemonListView(generic.ListView):
    """
    Displays a list of all available Pokémon.

    This view uses the PokemonService to retrieve all Pokémon and
    displays them in the 'abilitymanager/pokemon_list.html' template.

    Attributes:
        queryset: Queryset used to retrieve the list of Pokémon.
        template_name: Name of the template used to display the list of Pokémon.
    """

    queryset = PokemonService().get_all_pokemons()
    template_name = 'abilitymanager/pokemon_list.html'


class PokemonDetailView(generic.DetailView):
    """
    Displays the details of a specific Pokémon.

    This view uses the PokemonService to retrieve a Pokémon by its ID and
    displays the details in the 'abilitymanager/pokemon_detail.html' template.

    Attributes:
        template_name: Name of the template used to display the Pokémon details.
    """

    template_name = 'abilitymanager/pokemon_detail.html'

    def get_object(self) -> Pokemon:
        """
        Retrieves a Pokémon by its ID.

        Returns:
            Pokemon: The Pokémon found by its ID.
        """

        id: int = self.kwargs.get('pk')
        pokemon: Pokemon = PokemonService().find_pokemon_by_id(id=id)
        return pokemon


class AbilityCreateView(generic.CreateView):
    """
    Creates a new ability for a Pokémon.

    This view allows users to create a new ability for a specific Pokémon.
    It uses the PokemonAbilityService to create the ability and redirects to the
    Pokémon's detail page after creation.

    Attributes:
        model: Data model used for creation (in this case, PokemonAbility).
        fields: Form fields used for creation.
        template_name: Name of the template used for the creation form.
    """

    model = PokemonAbility
    fields = ['name']
    template_name = 'abilitymanager/ability_form.html'

    def form_valid(self, form):
        """
        Processes the creation form.

        Retrieves the Pokémon's ID from the URL, creates a new ability using the
        PokemonAbilityService, and redirects to the Pokémon's detail page.

        Args:
            form: Creation form.

        Returns:
            HttpResponseRedirect: Redirects to the Pokémon's detail page.
        """

        id: int = self.kwargs['pk']
        pokemon: Pokemon = PokemonService().find_pokemon_by_id(id=id)
        
        ability_name: str = form.cleaned_data['name']
        PokemonAbilityService().create_ability(name=ability_name, pokemon=pokemon)

        return redirect('pokemon-detail', pk=id)


class AbilityUpdateView(generic.UpdateView):
    """
    Updates an ability of a Pokémon.

    This view allows users to update an existing ability of a Pokémon.
    It uses the PokemonAbilityService to perform the update and redirects to the
    Pokémon's detail page after the update.

    Attributes:
        model: Data model used for the update (in this case, PokemonAbility).
        fields: Form fields used for the update.
        template_name: Name of the template used for the update form.
    """

    model = PokemonAbility
    fields = ['name']
    template_name = 'abilitymanager/ability_form.html'

    def form_valid(self, form):
        """
        Processes the update form.

        Retrieves the ability to be updated, updates the ability using the
        PokemonAbilityService, and redirects to the Pokémon's detail page.

        Args:
            form: Update form.

        Returns:
            HttpResponseRedirect: Redirects to the Pokémon's detail page.
        """

        ability: PokemonAbility = self.get_object()
        name: str = form.cleaned_data['name']

        PokemonAbilityService().update_ability(ability, name=name)

        return redirect('pokemon-detail', pk=ability.pokemon.id)


class AbilityDeleteView(generic.DeleteView):
    """
    Deletes an ability of a Pokémon.

    This view allows users to delete an ability of a Pokémon. It uses the
    PokemonAbilityService to perform the deletion and redirects to the Pokémon's
    detail page after the deletion.

    Attributes:
        model: Data model used for the deletion (in this case, PokemonAbility).
        template_name: Name of the template used for the delete confirmation.
        success_url: URL to which it redirects after the deletion (in this case, the
            Pokémon's detail page).
    """

    model = PokemonAbility
    template_name = 'abilitymanager/ability_form.html'
    success_url = reverse_lazy('pokemon-detail')

    def get(self, request, *args, **kwargs):
        """
        Processes the GET request to delete an ability.

        Redirects the request to the delete view.

        Args:
            request: GET request.

        Returns:
            HttpResponseRedirect: Redirects to the delete view.
        """

        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Performs the deletion of an ability.

        Retrieves the ability to be deleted, deletes the ability using the
        PokemonAbilityService, and redirects to the Pokémon's detail page.

        Args:
            request: DELETE request.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponseRedirect: Redirects to the Pokémon's detail page.
        """

        ability = self.get_object()

        PokemonAbilityService().delete_ability(ability)

        return redirect('pokemon-detail', pk=ability.pokemon.id)
