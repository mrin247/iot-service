import os
from celery import Celery

# import eventlet
# eventlet.monkey_patch()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edge.settings")


app = Celery("edge")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    "check-temp": {
        "task": "sensors.tasks.measure_temp_task",
        "schedule": 5,
    },
}

app.conf.beat_schedule = CELERY_BEAT_SCHEDULE
