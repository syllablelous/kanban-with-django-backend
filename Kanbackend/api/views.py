from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def entrypoint(request):
    """
    API entry point
    """
    data = {'message': "Welcome to the Kanbackend API."}
    return Response(data)


@api_view(['GET', 'POST'])
def tasks(request):
    """
    GET     - List all tasks 
    POST    - Create a new task
    """
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task(request, pk):
    """
    GET     - Get a specific task
    PUT     - Update the entire task
    PATCH   - Update a task partially
    DELETE  - Delete a task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            {'message': 'Task not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
        
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)