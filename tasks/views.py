from django.shortcuts import render,redirect
from .models import Task
from .forms import CreateTaskForm, UpdateTaskForm

# Create your views here.
def index(request): 
    tasks = Task.objects.all()
    
    if  request.method == 'POST': 
        form = CreateTaskForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/tasks')
    else:
        form = CreateTaskForm()
        
    context = {
        'tasks': tasks,
        'form': form
    }
        
    return render(request, 'tasks/lists.html', context)

def updateTask(request, pk): 
    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(instance=task);
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
             
    context = {'form': form}
    return render(request, 'tasks/update.html', context);

def deleteTask(request, pk): 
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST': 
        item.delete()
        return redirect('/tasks')
    return render(request, 'tasks/delete.html', context)