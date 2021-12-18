from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.TaskListCreateApiView.as_view(), name="task-list"),
	path('task-detail/<int:pk>/', views.TaskDetailRetrieveUpdateDestroyApiView.as_view(), name="task-detail"),
	path('task-create/', views.TaskListCreateApiView.as_view(), name="task-create"),
	path('task-update/<int:pk>/', views.TaskDetailRetrieveUpdateDestroyApiView.as_view(), name="task-update"),
	path('task-delete/<int:pk>/', views.TaskDetailRetrieveUpdateDestroyApiView.as_view(), name="task-delete"),
]