from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def work(request):
    return render(request, "hi.html")
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request,"password not matching")
            return redirect('/')
        return redirect('login')
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('work')
        else:
            messages.info(request, "Invalid credential")
            return redirect('login')

    return render(request,"login.html")