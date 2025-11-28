from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .maze import Maze


# Create your views here.



# def maze(request, size):
#     m = Maze(size)
#     m.generate()
#     m.solve()
#     # Convert path tuples to string keys so templates can test membership
#     # e.g. (2,3) -> "2,3"
#     path_keys = {f"{r},{c}" for (r, c) in m.path}
#     return render(request, 'maze_app/maze.html', {'grid': m.grid, 'path': path_keys})


# def maze(request, size, solve=False):
#     m = Maze(size)
#     m.generate()

#     path_keys = set()

#     if solve:
#         m.solve()
#         # Convert path tuples to string keys so templates can test membership
#         path_keys = {f"{r},{c}" for (r, c) in m.path}

#     return render(
#         request,
#         'maze_app/maze.html',
#         {
#             'grid': m.grid,
#             'path': path_keys,
#         }
#     )



from django.shortcuts import render
from django.http import JsonResponse
from .maze import Maze
import json


def maze(request, size, solve=False):
    m = Maze(size)
    m.generate()

    if solve:
        m.solve()

    # у шаблон для JS
    path = m.path if solve else []
    visited_order = m.visited_order if solve else []

    return render(
        request,
        'maze_app/maze.html',
        {
            'grid': m.grid,
            'size': size,
            'solve': solve,
            'path_json': json.dumps(path),
            'visited_json': json.dumps(visited_order),
        }
    )


def maze_json(request, size):
    """Експорт лабіринту в JSON."""
    m = Maze(size)
    m.generate()
    m.solve() 

    data = {
        'size': size,
        'grid': m.grid,
        'path': m.path,
    }
    return JsonResponse(data)
