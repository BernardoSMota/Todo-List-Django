from django.shortcuts import render, redirect
from todolist.models import Task

def index(request):
    tasks = Task.objects.all().order_by('-id')
    context = tasks
    return render(request=request, 
                  template_name='todolist/pages/index.html',
                  context={
                      'tasks':context,
                      }
                  )
    
def completed(request):
    tasks = Task.objects.filter(completed=True).order_by('-id')
    context = tasks
    return render(request=request, 
                  template_name='todolist/pages/index.html',
                  context={
                      'tasks':context,
                      'filter': 'completed'
                      }
                  )
    
def pending(request):    
    tasks = Task.objects.filter(completed=False).order_by('-id')
    context = tasks
    return render(request=request, 
                  template_name='todolist/pages/index.html',
                  context={
                      'tasks':context,
                      'filter': 'pending'
                      }
                  )
    
def changeCompleteStatus(request, id):

    task = Task.objects.filter(id=id).first()
    if task.completed:
        task.completed = False
    else:
        task.completed = True
        print('Entrou auqi')
        
    task.save()
    
    previous_url = request.META.get('HTTP_REFERER', 'todo:index')
    return redirect(previous_url)

def delete(request, id):
    task = Task.objects.filter(id=id).first()
    task.delete()
    
    previous_url = request.META.get('HTTP_REFERER', 'todo:index')
    return redirect(previous_url)