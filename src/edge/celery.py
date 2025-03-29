import os
from celery import Celery
from kombu import Queue, Exchange

# import eventlet
# eventlet.monkey_patch()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edge.settings")


app = Celery("edge")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

nodes = [
    "node-1",
    "node-2",
    "node-3"
]

CELERY_TASK_QUEUES = []
CELERY_BEAT_SCHEDULE = {}
for node in nodes:
    key = f"check-temp-{node}"
    CELERY_TASK_QUEUES.append(Queue(node, Exchange(node), routing_key=node))
    CELERY_BEAT_SCHEDULE[key] = {
        "task": "sensors.tasks.measure_temp_task",
        "schedule": 5,
        "options": {"queue": node}, # Apply async
    }
    
app.conf.task_queues = CELERY_TASK_QUEUES
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE
