from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def hello(request, name):
    # 1. Лічильник переглядів (session)
    views = request.session.get('views', 0)
    views += 1
    request.session['views'] = views

    cookies = request.COOKIES

    context = {
        "name": name,
        "views": views,
        "cookies": cookies,
    }

    response = render(request, "hello.html", context)

    response.set_cookie("author", "Zakaliuzhnyi")

    return response



def hello2(request):
    n = request.GET["name"]
    return HttpResponse(f"<h1>Hello {n}</h1>")

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def hello3(request):
    n = request.POST["name"]
    return HttpResponse(f"<h1>Hello {n}</h1>")
    



