from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .views import homepage, create_or_edit_task_list, view_list, create_new_task_post, delete_task_list_post, manage_task_lists, delete_task_list_post_manage, edit_task_list, edit_task_list_manage, set_importance_from_list, set_completed_from_list, edit_task, view_task_list_users, edit_task_list_users, delete_task_list_user_post, add_task_list_user, set_list_owner, assignedto_list, set_importance_from_assigned, set_completed_from_assigned, edit_assigned_task, todaytasks_list, set_importance_from_today, set_completed_from_today, edit_today_task, plannedtasks_list, set_importance_from_planned, set_completed_from_planned, edit_planned_task

urlpatterns = [
    path('', homepage, name="home"),
    path('manage_task_lists/', manage_task_lists, name="manage_task_lists"),
    path('view_list/<int:id>', view_list, name="view_list"),
    path('new_task_list/', create_or_edit_task_list, name="create_or_edit_task_list"),
    path('new_task/', create_new_task_post, name="create_new_task_post"),
    path('delete_list/<int:id>', delete_task_list_post, name="delete_task_list_post"),
    path('delete_list_from_manager/<int:id>', delete_task_list_post_manage, name="delete_task_list_post_manage"),
    path('edit_list/<int:id>', edit_task_list, name="edit_task_list"),
    path('edit_list_from_manager/<int:id>', edit_task_list_manage, name="edit_task_list_manage"),
    path('set_importance/<int:id>', set_importance_from_list, name="set_importance_from_list"),
    path('set_completed/<int:id>', set_completed_from_list, name="set_completed_from_list"),
    path('edit_task/<int:id>', edit_task, name="edit_task"),
    path('view_list_access/<int:id>', view_task_list_users, name="view_task_list_users"),
    path('edit_task_list_users/<int:id>', edit_task_list_users, name="edit_task_list_users"),
    path('delete_task_list_user_post/<int:id>', delete_task_list_user_post, name="delete_task_list_user_post"),
    path('add_task_list_user/<int:id>/', add_task_list_user, name="add_task_list_user"),
    path('set_list_owner/<int:id>', set_list_owner, name="set_list_owner"),
    path('assigned_to_list/', assignedto_list, name="assignedto_list"),
    path('set_assigned_importance/<int:id>', set_importance_from_assigned, name="set_importance_from_assigned"),
    path('set_assigned_completed/<int:id>', set_completed_from_assigned, name="set_completed_from_assigned"),
    path('edit_assigned_task/<int:id>', edit_assigned_task, name="edit_assigned_task"),
    path('today_tasks_list/', todaytasks_list, name="todaytasks_list"),
    path('set_today_importance/<int:id>', set_importance_from_today, name="set_importance_from_today"),
    path('set_today_completed/<int:id>', set_completed_from_today, name="set_completed_from_today"),
    path('edit_today_task/<int:id>', edit_today_task, name="edit_today_task"),
    path('planned_tasks_list', plannedtasks_list, name="plannedtasks_list"),
    path('set_planned_importance/<int:id>', set_importance_from_planned, name="set_importance_from_planned"),
    path('set_planned_completed/<int:id>', set_completed_from_planned, name="set_completed_from_planned"),
    path('edit_planned_task/<int:id>', edit_planned_task, name="edit_planned_task"),
]