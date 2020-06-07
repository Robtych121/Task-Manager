from django.contrib import admin
from .models import Task, Task_List, Task_List_Users

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_List)
admin.site.register(Task_List_Users)