from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from multiprocessing import Process, Pool
import time
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def millis():
    return int(round(time.time() * 1000))

def http_get(url):
    start_time = millis()
    result = {"url": url, "data": requests.get(url).text}
    return result


def multiprocessing(request):
    urls = ['http://www.google.com/', 'https://foursquare.com/', 'http://www.bing.com/',
            "https://www.yelp.com/"]
    pool = Pool(processes=5)

    start_time = millis()
    results = pool.map(http_get, urls)
    print("\nTotal took " + str(millis() - start_time) + " ms\n")
    for result in results:
        print(result)
    return JsonResponse(data={"response": results})
