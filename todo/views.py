from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo


def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/view-todo.html", {"todo": todo})


def todolist(request):
    todos = Todo.objects.all()

    return render(request, "todo/todolist.html", {"todos": todos})


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello django!")


def books(request):
    my_books = {1: "Python", 2: "Java", 3: "C# book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
