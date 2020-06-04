from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskListForm, CreateTaskForm, EditTaskListForm
from .models import Task_List, Task
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


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
            if(data.get('parent_list') == '0'):
                task_list.parent_list = None
            else:
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
    task_list = Task_List.objects.filter(id=id).first()
    if task_list.sort_by == 'Ascending':
        tasks = Task.objects.filter(list=task_list.id).order_by('name')
    else:
        tasks = Task.objects.filter(list=task_list.id).order_by('-name')
    users = User.objects.all()

    return render(request, 'view_task_list.html', {'tasks': tasks, 'task_list': task_list, 'users': users})


@require_http_methods(["POST"])
def create_new_task_post(request):
    """
    Creates new task from a posted form on task list
    """
    data = request.POST.copy()
    list_id = int(data.get('new_task_list_id'))
    task_list = Task_List.objects.filter(id=data.get('new_task_list_id')).first()

    task = Task(name=data.get('new_task'),list=task_list)
    task.save()

    return redirect('view_list', list_id)


def delete_task_list_post(request, id):
    """
    Deletes the selected list
    """
    task_list = Task_List.objects.get(pk=id)
    task_list.delete()
    return redirect('home')


def manage_task_lists(request):
    """
    Displays all task lists regardless of type
    """
    task_lists = Task_List.objects.all().order_by('name')

    return render(request, 'manage_task_lists.html', {'task_lists': task_lists})


def delete_task_list_post_manage(request, id):
    """
    Deletes the selected list and redirects to manage lists page
    """
    task_list = Task_List.objects.get(pk=id)

    if task_list.type == 'Normal':
        task_list.delete()
        return redirect('manage_task_lists')
    else:
        sublists = Task_List.objects.filter(parent_list=id)
        sublists.delete()
        task_list.delete()
        return redirect('manage_task_lists')


def edit_task_list(request, id):
    """
    Edits the current task list
    """
    task_list = Task_List.objects.get(pk=id)
    grouped_lists_select = Task_List.objects.filter(type='Group')

    if request.method == "POST":
        form = EditTaskListForm(request.POST, instance=task_list)

        if form.is_valid():
            form.save()
            return redirect('view_list', task_list.id)
    else:
        form = EditTaskListForm(instance=task_list)

    return render(request, "edit_task_list.html", {'grouped_lists_select': grouped_lists_select, 'form':form})


def edit_task_list_manage(request, id):
    """
    Edits the current task list from manager
    """
    task_list = Task_List.objects.get(pk=id)
    grouped_lists_select = Task_List.objects.filter(type='Group')

    if request.method == "POST":
        data = request.POST.copy()
        form = EditTaskListForm(request.POST, instance=task_list)
        
        if form.is_valid():
            task_list = form.save(commit=False)
            
            if data.get('parent_list') == 'None':
                task_list.parent_list = None
            else:
                task_list.parent_list = data.get('parent_list')

            task_list.save()
            return redirect('manage_task_lists')
    else:
        form = EditTaskListForm(instance=task_list)

    return render(request, "edit_task_list.html", {'task_list': task_list, 'grouped_lists_select': grouped_lists_select, 'form':form})