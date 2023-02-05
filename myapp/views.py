from django.shortcuts import render, redirect
from .form import signupform
from django.contrib.auth import authenticate, login

def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=signupform()
    return render(request, 'signup.html', {'form':form})

def loginview(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('next')
    return render(request, 'login.html')

def next(request):
    return render(request, 'next.html')