from django.forms import ModelForm
from .models import Todo


class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important"]
        # field = "__all__"
