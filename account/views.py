from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from home.views import home

# Create your views here.
def account(request):
        return render(request, 'account.html/')
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form':SignUpForm})

    else:
        if request.POST['password1'] == request.POST['password2']:           
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account:connectaccount')
            except IntegrityError:
                return render(request, 
                              'signup.html', 
                              {'form':SignUpForm,'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 
                          'signup.html', 
                          {'form':SignUpForm, 'error': 'Les mots de passe ne sont pas identiques'})
                  
def logoutaccount(request):
    logout(request)
    return redirect('account:signup')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', {'form': AuthenticationForm(), 'error': 'Utilisateur ou mot de passe incorrect'})
        else:
            login(request,user)
            return redirect('account:connectaccount')