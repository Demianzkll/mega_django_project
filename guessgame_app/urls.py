from django.urls import path
from . import views
from .views import guess_view, result_view


urlpatterns = [
    path("", guess_view, name="guess"),
    path("result/", result_view, name="result"),
]


