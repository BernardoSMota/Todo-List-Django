from django.shortcuts import render, redirect
from todoUser.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages


def createUser(request):
    form = RegisterForm()    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('todoUser:login')

    return render(request=request,
                  template_name='global/pages/login.html',
                  context={
                      'form': form,
                      'form-action': reverse('todoUser:create'),
                      'action': 'Create User',
                      'buttons': ['Cancelar', 'Criar']
                      }
                )
    
def loginUser(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user() 
            auth.login(request, user)
            messages.success(request, 'Usuário logado com sucesso!')
            
            return redirect('todo:index')
        else:
            messages.error(request, 'Login Inválido')
        
    return render(request=request,
                  template_name='global/pages/login.html',
                  context={
                      'form': form,
                      'action': 'Login',
                      'buttons': ['Cancelar', 'Entrar']
                      }
                )
    
def logoutUser(request):
    auth.logout(request)
    return redirect('todo:index')