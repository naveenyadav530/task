from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        age = request.POST['age']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email Exists")
            return redirect("register")
        elif password1 != password2:
            messages.info(request, "Password Not Matching..")
            return redirect("register")
        elif User.objects.filter(username=username):
            var = email.split("@")
            username = var[0]  
            print(username)  
            user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name, age=age)
            user.save()
            print("User Created")
            return redirect("login")
        else:
            user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
            user.save()
            print("User Created")
            return redirect("login")
           
    else:
        return render(request, "sign_up.html")


def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method  == "POST":
        username = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username = username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    else:
        return render(request, "login.html")
    