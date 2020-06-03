from .models import Task_List


def get_task_lists(request):
    task_lists = Task_List.objects.exclude(parent_list__isnull=False).order_by('name')
    return { 'nav_task_lists': task_lists}


def get_sub_task_lists(request):
    sub_task_lists = Task_List.objects.exclude(parent_list__isnull=True).order_by('name')
    return { 'sub_task_lists': sub_task_lists}