import logging

from django.core.mail import send_mail
from django.dispatch import Signal


logger: logging.Logger = logging.getLogger("django")


pokeapi_task_saved: Signal = Signal()
pokeapi_task_failed: Signal = Signal()


def executer_pokeapi_task_saved_signal(sender, **kwargs) -> None:
    """Exec function for pokeapi_task_saved signal.
    Sends an email with the Pokemon info.
    This signal is manually just executed from Celery tasks.

    Args:   
        - sender: Should be the celery task, but it's not validated.
    """

    send_mail(
        'New Pokemon from PokeAPI', 
        f'{kwargs["pokemon"]} was successfully created using PokeAPI',
        'admin@mail.local',
        ['admin@mail.local']
    )

def executer_pokeapi_task_failed_signal(sender, **kwargs) -> None:
    """Exec function for pokeapi_task_failed signal.
    Logs a repeated pokemon info into the poketasks.log file.

    Args:   
        - sender: Should be the celery task (when request fails), but it's not validated.
    """

    logger.info("Repeated pokemon was not created. Attributes: ")
    logger.info(kwargs["pokemon_attrs"])


# Connects executers with the custom signals
pokeapi_task_saved.connect(executer_pokeapi_task_saved_signal)
pokeapi_task_failed.connect(executer_pokeapi_task_failed_signal)

