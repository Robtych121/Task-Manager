from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskListForm
from .models import Task_List, Task


# Create your views here.
def create_or_edit_task_list(request, pk=None):
    """
    Create a view that allows us to create
    or edit a task list depending if the task list ID
    is null or not
    """
    grouped_lists = Task_List.objects.filter(type='Group')

    task_list = get_object_or_404(Task_List, pk=pk) if pk else None
    if request.method == 'POST':
        data = request.POST.copy()
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.parent_list = data.get('parent_list')
            task_list.save()
            return redirect('home')
    else:
        form = TaskListForm(instance=task_list)
    return render(request, 'task_list_form.html', {'form': form, 'grouped_lists': grouped_lists})


def view_list(request, id):
    """
    A view to show the list and the tasks associated to it
    """
    tasks = Task.objects.filter(list=id)

    return render(request, 'view_task_list.html', {'tasks': tasks})