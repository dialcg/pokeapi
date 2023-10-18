import random
import requests

from celery import shared_task
from celery.utils.log import get_task_logger

from django.urls import reverse_lazy

from core.signals import (
    pokeapi_task_failed,
    pokeapi_task_saved
)


logger = get_task_logger(__name__)


@shared_task
def extract_pokemon() -> None:
    """Extracts a pokemon from PokeAPI using a random ID from 1 to 100 and saves it to the app."""

    response: requests.Response = requests.get(
        f'https://pokeapi.co/api/v2/pokemon/{random.randint(1, 100)}' 
    )  

    if response.status_code == 200:
        pokemon_data: dict = response.json()
        url: str = 'http://localhost:8000' + reverse_lazy('api-pokemon-list-create')
        
        api_response: requests.Response = requests.post(
            url, 
            json=pokemon_data, 
            auth=('admin', 'admin')
        )

        if api_response.status_code == 201:
            logger.info(f'Pokemon succesfully saved. [name: {pokemon_data["name"]}]')
            pokeapi_task_saved.send(sender='extraer_pokemon', pokemon=pokemon_data["name"])
        elif api_response.status_code == 400:
            logger.info(f'Pokemon was not saved, trying a new one. [name: {pokemon_data["name"]}]')
            pokeapi_task_failed.send(sender='extraer_pokemon', pokemon_attrs=pokemon_data)
        
    else:
        logger.info('Error al extraer el Pokemon de https://pokeapi.co')
