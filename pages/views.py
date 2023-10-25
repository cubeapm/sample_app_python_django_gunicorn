from django.shortcuts import render
import redis
# import socket
import requests
# from kafka import KafkaConsumer, KafkaProducer
from django.db import connection
from django.http import HttpResponse
from django.http import Http404

redis_conn = redis.StrictRedis(host='redis', port=6379, db=0)
# kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092', client_id= socket.gethostname())
# kafka_consumer = KafkaConsumer('sample_topic', bootstrap_servers='kafka:9092', group_id='foo', auto_offset_reset='earliest')


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

# def kafka_produce(request):
#     try:
#         kafka_producer.send('sample_topic', b'raw_bytes')
#         return HttpResponse("Kafka produced")
#     except Exception as e:
#         return HttpResponse(f"Kafka production error: {str(e)}")

# def kafka_consume(request):
#     for msg in kafka_consumer:
#         return HttpResponse(str(msg.value))
#     return HttpResponse("No message")