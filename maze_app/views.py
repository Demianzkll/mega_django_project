from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .maze import Maze


# Create your views here.



def maze(request, size):
    m = Maze(size)
    m.generate()
    m.solve()
    # Convert path tuples to string keys so templates can test membership
    # e.g. (2,3) -> "2,3"
    path_keys = {f"{r},{c}" for (r, c) in m.path}
    return render(request, 'maze_app/maze.html', {'grid': m.grid, 'path': path_keys})
