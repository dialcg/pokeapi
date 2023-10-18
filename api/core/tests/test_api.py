from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Pokemon 


class PokemonAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)

    def test_create_pokemon(self):
        url = reverse('api-pokemon-list-create')  
        data = {
            'name': 'Pikachu',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pokemon.objects.count(), 1)
        self.assertEqual(Pokemon.objects.get().name, 'Pikachu')

    def test_get_pokemons(self):
        url = reverse('api-pokemon-list-create')  
        data = {
            'name': 'Bulbasaur'
        }
        self.client.post(url, data, format='json')
        url = reverse('api-pokemon-list-create') 

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Bulbasaur')

    def test_get_filtered_pokemon_if_q_exists(self):
        pokemon_to_create = [
            Pokemon(name='Pikachu'),
            Pokemon(name='Charizard'),
            Pokemon(name='Bulbasaur'),
        ]

        Pokemon.objects.bulk_create(pokemon_to_create)

        url = reverse('api-pokemon-list-create')  
        response = self.client.get(url, {'q': 'Pikachu'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Pikachu')