from django import forms
from .models import Task_List, Task

class TaskListForm(forms.ModelForm):
    class Meta:
        model = Task_List
        fields = ('name', 'type')

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)


class EditTaskListForm(forms.ModelForm):
    class Meta:
        model = Task_List
        fields = ('name', 'sort_by')