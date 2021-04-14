from django import forms
from todolist_app.models import Todolist

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ["task" , "done"]