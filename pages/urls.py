# pages/urls.py
from django.urls import path

from .views import home_page_view
from .views import custom_404_view
from .views import set_redis_value
from .views import api_view
from .views import mysql_view
from .views import kafka_produce
from .views import KafkaConsumerCommand
urlpatterns = [
    path("", home_page_view, name="home"),
    path("exception/" , custom_404_view, name="exception"),
    path("redis/", set_redis_value, name="redis"),
    path("api/", api_view, name="API"),
    path("mysql/", mysql_view, name="MYSQL"),
    path("kafka/produce/" , kafka_produce, name="Produce"),
    path("kafka/consume/" , KafkaConsumerCommand, name= "Consume")
]