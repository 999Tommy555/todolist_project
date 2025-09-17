from django.forms import ModelForm
from .models import Todo


class CreateTodoform(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important"]


class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important", "completed"]
        # field = "__all__"
