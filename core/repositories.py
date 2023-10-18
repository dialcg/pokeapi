from .models import (
    Pokemon,
    PokemonAbility
)


class PokemonRepository:
    """Manages entitie access for Pokemon records."""

    def create_pokemon(self,name: str) -> Pokemon:
        """Creates a new Pokemon record."""

        return Pokemon.objects.create(name=name)


    def get_all_pokemons(self) -> list[Pokemon]:
        """Gets all pokemons."""

        return Pokemon.objects.all()


    def find_pokemon_by_name(self, name: str) -> Pokemon:
        """Gets a pokemon by name."""

        try:
            return Pokemon.objects.get(name=name)
        except Pokemon.DoesNotExist:
            return None
        

    def find_pokemon_by_id(self, id: int) -> Pokemon:
        """Gets a pokemon by PK/ID."""

        try:
            return Pokemon.objects.get(id=id)
        except Pokemon.DoesNotExist:
            return None


class PokemonAbilityRepository:
    """Manages entity access for PokemonAbility records."""

    def create_ability(self, name: str, pokemon):
        """Creates a new PokemonAbility record."""

        return PokemonAbility.objects.create(name=name, pokemon=pokemon)

    def get_all_abilities(self):
        """Gets all Pokemon abilities."""

        return PokemonAbility.objects.all()

    def find_ability_by_id(self, id: int):
        """Gets a PokemonAbility by PK/ID."""

        try:
            return PokemonAbility.objects.get(id=id)
        except PokemonAbility.DoesNotExist:
            return None

    def update_ability(self, ability, name):
        """Updates the name of a PokemonAbility."""

        ability.name = name
        ability.save()

    def delete_ability(self, ability):
        """Deletes a PokemonAbility."""

        ability.delete()
