import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poketasks.settings")

app = Celery("poketasks", broker='redis://localhost:6379/0')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()