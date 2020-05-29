from django.contrib.auth import views
from django.urls import path
from .views import create_or_edit_task_list

urlpatterns = [
    path('new_task_list/', create_or_edit_task_list, name="create_or_edit_task_list")
]