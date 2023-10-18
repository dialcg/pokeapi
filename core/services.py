from .models import Pokemon
from .repositories import (
    PokemonRepository,
    PokemonAbilityRepository
)


class PokemonService:
    """A service that manages Pokemon CRUD operations.

    This service provides methods to create, retrieve, and search for Pokemon
    records in the database.

    Attributes:
        repo (PokemonRepository): An instance of the PokemonRepository used to
        interact with the database.
    """

    def __init__(self):
        """Initialize the PokemonService with a PokemonRepository instance."""

        self.repo = PokemonRepository()

    def create_pokemon(self, name: str) -> Pokemon:
        """Create a new Pokemon record in the database and capitalizes its name.

        Args:
            name (str): The name of the Pokemon to create.

        Returns:
            Pokemon: The created Pokemon instance.
        """

        name: str = name.capitalize()

        return self.repo.create_pokemon(name=name)

    def get_all_pokemons(self) -> list[Pokemon]:
        """Retrieve a list of all Pokemon records in the database.

        Returns:
            list[Pokemon]: A list of all Pokemon instances.
        """

        return self.repo.get_all_pokemons()

    def find_pokemon_by_name(self, name: str) -> Pokemon:
        """Search for a Pokemon by its name in the database.

        Args:
            name (str): The name of the Pokemon to search for.

        Returns:
            Pokemon: The found Pokemon instance, or None if not found.
        """

        return self.repo.find_pokemon_by_name(name=name)

    def find_pokemon_by_id(self, id: int) -> Pokemon:
        """Search for a Pokemon by its ID in the database.

        Args:
            id (int): The ID of the Pokemon to search for.

        Returns:
            Pokemon: The found Pokemon instance, or None if not found.
        """

        return self.repo.find_pokemon_by_id(id=id)


class PokemonAbilityService:
    """A service that manages PokemonAbility CRUD operations.

    This service provides methods to create, retrieve, and search for PokemonAbility
    records in the database.

    Attributes:
        repo (PokemonAbilityRepository): An instance of the PokemonAbilityRepository used to
        interact with the database.
    """

    def __init__(self):
        """Initialize the PokemonAbilityService with a PokemonAbilityRepository instance."""

        self.repo = PokemonAbilityRepository()

    def create_ability(self, name: str, pokemon):
        """Create a new PokemonAbility record in the database.

        Args:
            name (str): The name of the PokemonAbility to create.
            pokemon (Pokemon): The Pokemon instance to associate with the ability.

        Returns:
            PokemonAbility: The created PokemonAbility instance.
        """

        return self.repo.create_ability(name=name, pokemon=pokemon)

    def get_all_abilities(self):
        """Retrieve a list of all PokemonAbility records in the database.

        Returns:
            list[PokemonAbility]: A list of all PokemonAbility instances.
        """

        return self.repo.get_all_abilities()

    def find_ability_by_id(self, id: int):
        """Search for a PokemonAbility by its ID in the database.

        Args:
            id (int): The ID of the PokemonAbility to search for.

        Returns:
            PokemonAbility: The found PokemonAbility instance, or None if not found.
        """

        return self.repo.find_ability_by_id(id=id)

    def update_ability(self, ability, name):
        """Update the name of a PokemonAbility.

        Args:
            ability (PokemonAbility): The PokemonAbility instance to update.
            name (str): The new name for the ability.
        """

        return self.repo.update_ability(ability, name)

    def delete_ability(self, ability):
        """Delete a PokemonAbility record from the database.

        Args:
            ability (PokemonAbility): The PokemonAbility instance to delete.
        """

        return self.repo.delete_ability(ability)