from django.utils import timezone
import helpers
from . import collect
from django.apps import apps
from celery import shared_task

@shared_task
def measure_temp_task():
    # print("Collecting temperature")
    Metric = apps.get_model("sensors", "Metric")
    temp = collect.get_random_temperature()
    node_id = helpers.config("NODE_ID", default=0)
    # print(f"Collecting temperature: {temp} for node {node_id}")
    Metric.objects.create(
        node_id=node_id,
        temperature=temp,
        time=timezone.now()
    )

