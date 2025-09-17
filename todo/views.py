from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import Todoform, CreateTodoform
from datetime import datetime


def create_todo(request):
    message = ""
    form = CreateTodoform()
    if request.method == "POST":
        form = CreateTodoform(request.POST)
        form.save()
        message = "建立成功!"
        return redirect("todolist")

    return render(request, "todo/create-todo.html", {"message": message, "form": form})


def delete_todo(request, id):
    # 檢視日期
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except Exception as e:
        print(e)

    return redirect("todolist")


def view_todo(request, id):
    message = ""
    try:
        todo = Todo.objects.get(id=id)
        form = Todoform(instance=todo)
    except Exception as e:
        print(e)

    if request.method == "POST":

        form = Todoform(request.POST, instance=todo)
        todo = form.save(commit=False)

        if todo.completed:
            todo.date_completed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            todo.date_completed = None
        todo.save()
        message = "更新成功!"

    return render(
        request, "todo/view-todo.html", {"todo": todo, "form": form, "message": message}
    )


def todolist(request):
    # order_by 加上 - 號降序
    todos = Todo.objects.all().order_by("-created")

    return render(request, "todo/todolist.html", {"todos": todos})


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello django!")


def books(request):
    my_books = {1: "Python", 2: "Java", 3: "C# book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
