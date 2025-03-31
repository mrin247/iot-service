from datetime import datetime
from typing import List
from ninja import NinjaAPI, Schema

from sensors import services

api = NinjaAPI()

class AvgTempSchema(Schema): # pydantic
    average_temp: float
    time_group: datetime
    
class NodeAvgTempSchema(Schema):
    node_id: int# pydantic
    average_temp: float
    time_group: datetime
    
class MaxMinTempSchema(Schema):
    max_temp: float
    min_temp: float

class NodeMaxMinTempSchema(Schema):
    node_id: int
    max_temp: float
    min_temp: float

@api.get('/temps', response=List[AvgTempSchema])
def get_average_temps(request):
    qs = services.get_average_temp()
    return qs


@api.get('/temps/nodes', response=List[NodeAvgTempSchema])
def get_average_temps(request):
    qs = services.get_node_average_temp()
    return qs

@api.get('/temps/maxmin', response=MaxMinTempSchema)
def get_average_temps(request):
    qs = services.get_max_min_temp()
    return qs

@api.get('/temps/nodes/maxmin', response=List[NodeMaxMinTempSchema])
def get_average_temps(request):
    qs = services.get_node_max_min_temp()
    return qs