from django import forms
from .models import Task_List, Task
import html5.forms.widgets as html5_widgets

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


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date', 'importance', 'completed')
        widgets = {
            'due_date': html5_widgets.DateInput
        }