from django.shortcuts import render
import redis
from django.db import connections
from pages.models import Users, Person 
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from kafka import KafkaConsumer, KafkaProducer
from django.db import connection
from django.http import HttpResponse
from django.http import Http404

redis_conn = redis.StrictRedis(host='redis', port=6379, db=0)

def home_page_view(request):
    return HttpResponse("Hello")


def custom_404_view(request):
    raise Http404("This is a custom 404 error message")


def set_redis_value(request):
    redis_conn.set('foo', 'bar')
    return HttpResponse("Redis called")


def api_view(request):
    response = requests.get('http://localhost:8000/')
    return HttpResponse("API called")


def mysql_view(request):
    # Use the 'default' database connection
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT NOW()")
        data = cursor.fetchall()
    
    # Process and format the data as needed
    response_data = "\n".join([str(row) for row in data])
    return HttpResponse(response_data)


def kafka_produce(request):
    producer = KafkaProducer(**settings.KAFKA_PRODUCER_SETTINGS)
    producer.send('sample_topic', b'raw_bytes')
    return HttpResponse("Kafka produced")


class KafkaConsumerCommand(BaseCommand):
    help = 'Starts the Kafka consumer'

    def handle(self, *args, **options):
        consumer = KafkaConsumer('sample_topic', **settings.KAFKA_CONSUMER_SETTINGS)

        for message in consumer:
            # Handle Kafka messages here
            deserialized_data = message.value
            print(deserialized_data)
