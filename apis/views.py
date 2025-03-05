import requests
from django.core.cache import cache
from django.http import HttpResponse
from apis.models import User
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://mongo:27017/")


def index(request):
    return HttpResponse("Hello")


def param(request, param):
    return HttpResponse("Got param {}".format(param))


def exception(request):
    raise Exception("Sample exception")


def api(request):
    requests.get('http://localhost:8000/apis/')
    return HttpResponse("API called")


def redis(request):
    cache.set('foo', 'bar')
    return HttpResponse("Redis called")


def mysql(request):
    return HttpResponse(User.objects.all())


def mongo(request):
    post_id = mongoClient.test_database.test_collection.insert_one(
        {'key1': 'value1'}).inserted_id
    return HttpResponse(str(post_id))
