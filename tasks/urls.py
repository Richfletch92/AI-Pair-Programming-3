from django.urls import path
from .views import task_list, update_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('tasks/<int:task_id>/update/', update_task, name='update_task'),
]