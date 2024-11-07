from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter a task here", 
                "class": "form-control", 
                "autofocus": True
            }
        )
    )
    description = forms.CharField(
        required=True, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter task description here", 
                "class": "form-control",
                "rows": 3
            }
        )
    )
    assignee_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter assignee name here", 
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter user email here", 
                "class": "form-control"
            }
        )
    )
    
    class Meta:
        model = Task
        fields = ('title', 'description', 'assignee_name', 'email', 'deadline', 'typex')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
