from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import Task
from datetime import datetime
from django.urls import reverse

def index(request):
    user = request.user
    context = {
        'user': user
    }

    if user.is_authenticated:
        tasks = Task.objects.filter(owner=user).order_by('-id', )
        context['tasks'] = tasks

            
    return render(request=request, 
                template_name='todolist/pages/index.html',
                context=context
                )
    
    
def completed(request):
    user = request.user
    context = {
        'user': user,
        'filter': 'completed',
    }
    
    if user.is_authenticated:    
        tasks = Task.objects.filter(completed=True, owner=user).order_by('-id')
        context['tasks'] = tasks
        
    return render(request=request, 
                  template_name='todolist/pages/index.html',
                  context=context
                  )

    
def pending(request):    
    user = request.user
    context = {
        'user': user,
        'filter': 'pending'
    }
    if user.is_authenticated:   
        tasks = Task.objects.filter(completed=False, owner=user).order_by('-id')
        context['tasks'] = tasks
        
        
    return render(request=request, 
                  template_name='todolist/pages/index.html',
                  context=context
                )
    

def createTask(request):
    form_action = reverse('todo:create')
    user = request.user
    
    if user.is_authenticated  and request.method == 'POST':
        task_title = request.POST.get('task_title')
        
        if task_title:
            new_task = Task(title=task_title, owner=user)
            new_task.save()
        
            return redirect('todo:index')
    
    context = {
        'action': 'Create',
        'form-action': form_action
    }
    
    return render(request=request, template_name='todolist/pages/new_task.html', context=context)


def editTask(request, id):
    task = get_object_or_404(Task, id=id)
    
    form_action = reverse('todo:edit', args=(id,))
    task_title = task.title
    
    context = {
        'title': task_title,
        'action': 'Edit',
        'form_action': form_action,
    }
    
    if request.method == 'POST':
        new_task_title = request.POST.get('task_title')
        task.title = new_task_title
        task.save()
        
        return redirect('todo:index')
    
    return render(request=request, template_name='todolist/pages/new_task.html', context=context)


def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()

    previous_url = request.META.get('HTTP_REFERER', 'todo:index')
    return redirect(previous_url)


def changeCompleteStatus(request, id):


    task = get_object_or_404(Task, id=id)
    if task.completed:
        task.completed = False
        task.completed_at = None
    else:
        task.completed = True
        current_time = datetime.now()
        task.completed_at = current_time
        
    task.save()
    
    previous_url = request.META.get('HTTP_REFERER', 'todo:index')
    return redirect(previous_url)