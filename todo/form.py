from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Todo

User = get_user_model()

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = [
            "title",
            "content",
            "completed"
        ]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

