from django.contrib import admin
from .models import Task, Task_List

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_List)