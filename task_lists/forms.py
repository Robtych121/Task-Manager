from django import forms
from .models import Task_List

class TaskListForm(forms.ModelForm):
    class Meta:
        model = Task_List
        fields = ('name', 'type')