from .models import Task_List


def get_task_lists(request):
    task_lists = Task_List.objects.all().order_by('name')
    return { 'task_lists': task_lists}