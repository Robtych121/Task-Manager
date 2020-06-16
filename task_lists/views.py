from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskListForm, CreateTaskForm, EditTaskListForm, EditTaskForm, EditTaskListUserForm
from .models import Task_List, Task, Task_List_Users
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    task_lists = Task_List.objects.all()

    assignedtocount = Task.objects.filter(assigned_to=request.user.id).count()
    todaysdate = datetime.today()
    todaycount = Task.objects.filter(assigned_to=request.user.id, due_date=todaysdate).count()
    futurecount = Task.objects.filter(assigned_to=request.user.id, due_date__gt=todaysdate).count() 
    pastcount = Task.objects.filter(assigned_to=request.user.id, due_date__lt=todaysdate).count() 
    importancecount = Task.objects.filter(assigned_to=request.user.id, importance='Yes').count()
    taskscount = Task.objects.filter(assigned_to=request.user.id, list=None).count()

    return render(request, 'home.html', {'home_task_lists': task_lists, 'assignedtocount': assignedtocount, 'todaycount': todaycount, 'futurecount': futurecount, 'pastcount': pastcount, 'importancecount': importancecount, 'taskscount': taskscount})


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
            task_list.list_owner = request.user.id
            task_list.save()
            TaskListUsers = Task_List_Users(list_id=task_list.id, user_id=request.user.id, perm_view="Yes", perm_add="Yes", perm_edit="Yes", perm_delete="Yes")
            TaskListUsers.save()
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
        tasks = Task.objects.exclude(completed='Yes').filter(list=task_list.id).order_by('name')
        completedtasks = Task.objects.exclude(completed='No').filter(list=task_list.id).order_by('name')
    else:
        tasks = Task.objects.exclude(completed='Yes').filter(list=task_list.id).order_by('-name')
        completedtasks = Task.objects.exclude(completed='No').filter(list=task_list.id).order_by('-name')
    users = User.objects.all()

    return render(request, 'view_task_list.html', {'tasks': tasks, 'completedtasks': completedtasks, 'task_list': task_list, 'users': users})


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
    tasklistusers = Task_List_Users.objects.filter(list_id=id)
    
    tasklistusers.delete()
    task_list.delete()
    return redirect('home')


def manage_task_lists(request):
    """
    Displays all task lists regardless of type
    """
    task_lists = Task_List.objects.all().order_by('name')
    task_listnames = Task_List.objects.all().order_by('name')


    return render(request, 'manage_task_lists.html', {'task_lists': task_lists, 'task_listnames': task_listnames})


def delete_task_list_post_manage(request, id):
    """
    Deletes the selected list and redirects to manage lists page
    """
    task_list = Task_List.objects.get(pk=id)
    tasklistusers = Task_List_Users.objects.filter(list_id=id)

    if task_list.type == 'Normal':
        tasklistusers.delete()
        task_list.delete()
        return redirect('manage_task_lists')
    else:
        sublistsid = Task_List.objects.filter(parent_list=id).values_list('id')
        subtasklistusers = Task_List_Users.objects.filter(list_id__in=sublistsid)
        subtasklistusers.delete()
        sublists = Task_List.objects.filter(parent_list=id)
        sublists.delete()
        tasklistusers.delete()
        task_list.delete()
        return redirect('manage_task_lists')


def edit_task_list(request, id):
    """
    Edits the current task list
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
            return redirect('view_list', task_list.id)
    else:
        form = EditTaskListForm(instance=task_list)

    return render(request, "edit_task_list.html", {'task_list': task_list, 'grouped_lists_select': grouped_lists_select, 'form':form})


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


def set_importance_from_list(request, id):
    """
    Sets the importance flag from task list
    """

    task = Task.objects.get(pk=id)
    importance = 'importance' + str(task.id)

    if request.method == 'POST':
        data = request.POST.copy()
        if data.get(importance) == None:
            task.importance = 'No'
        else:
            task.importance = 'Yes'
        task.save()
        return redirect('view_list', task.list.id)


def set_completed_from_list(request, id):
    """
    Sets the completed flag from task list
    """

    task = Task.objects.get(pk=id)
    completed = 'completed' + str(task.id)

    if request.method == 'POST':
        data = request.POST.copy()
        if data.get(completed) == None:
            task.completed = 'No'
        else:
            task.completed = 'Yes'
        task.save()
        return redirect('view_list', task.list.id)


def edit_task(request, id):
    """
    opens up edit form for when click into a task
    """

    task = Task.objects.get(pk=id)
    tasklistusers = Task_List_Users.objects.filter(list_id=task.list.id)
    users = User.objects.all()

    if request.method == "POST":
        data = request.POST.copy()
        form = EditTaskForm(request.POST, instance=task)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = data.get('assigned_to')
            task.save()
            return redirect('view_list', task.list.id)
    else:
        form = EditTaskForm(instance=task)

    return render(request, "edit_task.html", {'task': task, 'tasklistusers': tasklistusers, 'users': users, 'form':form})


def view_task_list_users(request, id):
    """
    Opens up the list of users for a task list
    """

    tasklist = Task_List.objects.get(pk=id)
    tasklistusers = Task_List_Users.objects.filter(list_id=id)
    users = User.objects.all()

    return render(request, "view_task_list_users.html", {'tasklistusers': tasklistusers, 'users': users, 'tasklist': tasklist})


def edit_task_list_users(request, id):
    """
    opens up edit form for when click into a task list user
    """

    tasklistuser = Task_List_Users.objects.get(pk=id)

    if request.method == "POST":
        data = request.POST.copy()
        form = EditTaskListUserForm(request.POST, instance=tasklistuser)
        
        if form.is_valid():
            tasklistuser = form.save(commit=False)

            tasklistuser.save()
            return redirect('view_task_list_users', tasklistuser.list_id)
    else:
        form = EditTaskListUserForm(instance=tasklistuser)

    return render(request, "edit_task_list_user.html", {'tasklistuser': tasklistuser, 'form':form})


def delete_task_list_user_post(request, id):
    """
    Deletes the selected list user
    """

    task_list_used = Task_List_Users.objects.get(pk=id)

    task_list_user = Task_List_Users.objects.get(pk=id)
    task_list_user.delete()
    return redirect('view_task_list_users', task_list_used.list_id)


def add_task_list_user(request, id):
    """
    Adds a user to the task list users permissions
    """

    tasklistusers = Task_List_Users.objects.filter(list_id=id).values_list('user_id')
    listsusers = User.objects.exclude(id__in=tasklistusers)

    if request.method == "POST":
        data = request.POST.copy()
        form = EditTaskListUserForm(request.POST)
        
        if form.is_valid():
            tasklistuser = form.save(commit=False)
            tasklistuser.list_id = id
            tasklistuser.user_id = data.get('user_id')
            tasklistuser.save()
            return redirect('view_task_list_users', id)
    else:
        form = EditTaskListUserForm()

    return render(request, "create_task_list_user.html", {'tasklistusers': tasklistusers, 'listsusers': listsusers, 'form':form})

def set_list_owner(request, id):
    """
    Sets the user as the list owner
    """
    tasklistuser = Task_List_Users.objects.get(id=id)
    tasklist = Task_List.objects.get(id=tasklistuser.list_id)


    tasklist.list_owner = tasklistuser.user_id
    tasklist.save()

    return redirect('view_task_list_users', tasklistuser.list_id)


def assignedto_list(request):
    """
    A view to show the assigned tolist and the tasks associated to it
    """
    user_id = request.user.id
    tasks = Task.objects.exclude(completed='Yes').filter(assigned_to=user_id).order_by('name')
    completedtasks = Task.objects.exclude(completed='No').filter(assigned_to=user_id).order_by('name')
    users = User.objects.all()

    return render(request, 'view_task_assignedto_list.html', {'tasks': tasks, 'completedtasks': completedtasks, 'users': users})