from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def hello(request, name):
    print(type(request), type(HttpRequest()))
    return HttpResponse(f"<h1>Hello {name}</h1>")

def hello2(request):
    n = request.GET["name"]
    return HttpResponse(f"<h1>Hello {n}</h1>")

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def hello3(request):
    n = request.POST["name"]
    return HttpResponse(f"<h1>Hello {n}</h1>")
    