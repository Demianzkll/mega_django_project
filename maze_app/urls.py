from django.urls import path
from . import views

urlpatterns = [
    path('<int:size>/', views.maze, {'solve': False}, name='maze'),
    path('<int:size>/solve/', views.maze, {'solve': True}, name='maze_solve'),
    path('<int:size>/json/', views.maze_json, name='maze_json'),
]
