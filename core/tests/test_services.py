from django.test import TestCase
from core.models import Pokemon, PokemonAbility
from core.services import PokemonService


class PokemonServiceTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pikachu = Pokemon.objects.create(name="Pikachu")
        cls.charizard = Pokemon.objects.create(name="Charizard")

        PokemonAbility.objects.create(pokemon=cls.pikachu, name="Static")
        PokemonAbility.objects.create(pokemon=cls.pikachu, name="Lightning Rod")
        PokemonAbility.objects.create(pokemon=cls.charizard, name="Blaze")
        PokemonAbility.objects.create(pokemon=cls.charizard, name="Solar Power")

    def test_create_pokemon(self):
        service = PokemonService()
        new_pokemon = service.create_pokemon(name="Bulbasaur")

        self.assertEqual(new_pokemon.name, "Bulbasaur")
        self.assertIsInstance(new_pokemon, Pokemon)
        self.assertEqual(Pokemon.objects.filter(name="Bulbasaur").count(), 1)

    def test_get_all_pokemons(self):
        service = PokemonService()
        all_pokemons = service.get_all_pokemons()

        self.assertEqual(len(all_pokemons), 2) 
        self.assertEqual(set(pokemon.name for pokemon in all_pokemons), {"Pikachu", "Charizard"})

    def test_find_pokemon_by_name(self):
        service = PokemonService()
        found_pokemon = service.find_pokemon_by_name(name="Pikachu")

        self.assertEqual(found_pokemon.name, "Pikachu")

        not_found_pokemon = service.find_pokemon_by_name(name="Squirtle")
        self.assertIsNone(not_found_pokemon)

    def test_find_pokemon_by_id(self):
        service = PokemonService()
        found_pokemon = service.find_pokemon_by_id(id=self.pikachu.id)
        
        self.assertEqual(found_pokemon.name, "Pikachu")

        not_found_pokemon = service.find_pokemon_by_id(id=10)
        self.assertIsNone(not_found_pokemon)
