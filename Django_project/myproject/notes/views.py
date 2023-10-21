from django.shortcuts import render
from rest_framework.decorators import api_view #to support the specific request type
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


@api_view(['GET'])
def api_overview(request):# to display the supported urls
    api_urls={
        'List':'/task-list/',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/create-task/',
        'Update':'/update-task/<str:pk>/',
        'Delete':'/delete-task/<str:pk>/'
    }
    return Response(api_urls)

# Below Function going to display all the tasks store in the data base.
@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()#collecting all tasks
    serializer=TaskSerializer(tasks,many=True)#converting all tasks into json format
    return Response(serializer.data)#sending the data to the client

# This Function going to display Detailed view of one perticuler task with the help of pk.
@api_view(['GET'])
def task_detail(request,pk):
    task=Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def update_task(request,pk):
    task=Task.objects.get(id=pk)
    serializer =TaskSerializer(instance=task,data=request.data)#updating the task details
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('task deleted successfully!')

