from django.contrib.auth import views
from django.urls import path
from .views import create_or_edit_task_list, view_list, create_new_task_post, delete_task_list_post, manage_task_lists, delete_task_list_post_manage, edit_task_list, edit_task_list_manage, set_importance_from_list

urlpatterns = [
    path('manage_task_lists/', manage_task_lists, name="manage_task_lists"),
    path('view_list/<int:id>', view_list, name="view_list"),
    path('new_task_list/', create_or_edit_task_list, name="create_or_edit_task_list"),
    path('new_task/', create_new_task_post, name="create_new_task_post"),
    path('delete_list/<int:id>', delete_task_list_post, name="delete_task_list_post"),
    path('delete_list_from_manager/<int:id>', delete_task_list_post_manage, name="delete_task_list_post_manage"),
    path('edit_list/<int:id>', edit_task_list, name="edit_task_list"),
    path('edit_list_from_manager/<int:id>', edit_task_list_manage, name="edit_task_list_manage"),
    path('set_importance/<int:id>', set_importance_from_list, name="set_importance_from_list"),
]