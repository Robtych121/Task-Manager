from django.contrib.auth import views
from django.urls import path
from .views import create_or_edit_task_list, view_list, create_new_task_post, delete_task_list_post, manage_task_lists

urlpatterns = [
    path('manage_task_lists/', manage_task_lists, name="manage_task_lists"),
    path('view_list/<int:id>', view_list, name="view_list"),
    path('new_task_list/', create_or_edit_task_list, name="create_or_edit_task_list"),
    path('new_task/', create_new_task_post, name="create_new_task_post"),
    path('delete_list/<int:id>', delete_task_list_post, name="delete_task_list_post"),
]