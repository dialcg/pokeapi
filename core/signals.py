import logging

from django.core.mail import send_mail
from django.dispatch import Signal


logger = logging.getLogger("django")


pokeapi_task_saved = Signal()
pokeapi_task_failed = Signal()


def executer_pokeapi_task_saved_signal(sender, **kwargs):
    """Exec function for pokeapi_task_saved signal."""

    send_mail(
        'New Pokemon from PokeAPI', 
        f'{kwargs["pokemon"]} was successfully created using PokeAPI',
        'admin@mail.local',
        ['admin@mail.local']
    )

def executer_pokeapi_task_failed_signal(sender, **kwargs):
    """Exec function for pokeapi_task_failed signal."""
    logger.info("Repeated pokemon was not created. Attributes: ")
    logger.info(kwargs["pokemon_attrs"])


# Connects executers with the custom signals
pokeapi_task_saved.connect(executer_pokeapi_task_saved_signal)
pokeapi_task_failed.connect(executer_pokeapi_task_failed_signal)

