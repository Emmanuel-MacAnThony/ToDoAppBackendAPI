from ..models import Task
from rest_framework import generics
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<int:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<int:pk>/',
		'Delete':'/task-delete/<int:pk>/',
		}

	return Response(api_urls)

class TaskListCreateApiView(generics.ListCreateAPIView): 
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
class TaskDetailRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    