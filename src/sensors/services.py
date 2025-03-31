from datetime import datetime, timedelta
from django.utils import timezone

from django.db.models import Avg, Max, Min
from django.db.models.functions import TruncMinute


from sensors.models import Metric

def get_average_temp():
    now = timezone.now()
    start_range = now - timedelta(days=1)

    metrics_query = (
        Metric.timescale
        .filter(time__range=(start_range, now))
        .annotate(time_group=TruncMinute("time"))
        .values("time_group")
        .annotate(average_temp=Avg("temperature"))
        .order_by("time_group")
    )

    return metrics_query

def get_node_average_temp():
    now = timezone.now()
    start_range = now - timedelta(days=1)

    metrics_query = (
        Metric.timescale
        .filter(time__range=(start_range, now))
        .annotate(time_group=TruncMinute("time"))
        .values("time_group",'node_id')
        .annotate(average_temp=Avg("temperature"))
        .order_by("time_group","node_id")
    )

    return metrics_query


def get_max_min_temp():
    now = timezone.now()
    start_range = now - timedelta(days=1)

    metrics_query = (
        Metric.timescale
        .filter(time__range=(start_range, now))
        .aggregate(
            max_temp=Max("temperature"),
            min_temp=Min("temperature")
        )
    )

    return metrics_query

def get_node_max_min_temp():
    now = timezone.now()
    start_range = now - timedelta(days=1)

    metrics_query = (
        Metric.timescale
        .filter(time__range=(start_range, now))
        .values("node_id")
        .annotate(
            max_temp=Max("temperature"),
            min_temp=Min("temperature")
        )
        .order_by("node_id")
    )

    return metrics_query

