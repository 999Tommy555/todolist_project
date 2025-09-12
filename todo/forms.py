from django.forms import ModelForm
from .models import Todo


class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important", "completed"]
        # field = "__all__"
