from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'Date','completed']

        widgets = {
            'Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
