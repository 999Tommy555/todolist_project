from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo


def todolist(request):
    todos = Todo.objects.all()

    return render(request, "todo/todolist.html", {"todos": todos})


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello django!")


def books(request):
    my_books = {1: "Python", 2: "Java", 3: "C# book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
