from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_overview,name='api_overview'),
    path('task-list/',views.taskList,name='task-list'),
    path('task-detail/<str:pk>/',views.task_detail,name='task-details'),
    path('update-task/<str:pk>/',views.update_task,name='update-task'),
    path('create-task/', views.create_task, name='create_task'),
    path('delete-task/<str:pk>/',views.delete_task,name='delete-task'),
]