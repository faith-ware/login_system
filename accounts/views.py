from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm, Userform
import re

# Create your views here.


def home(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    if request.user.is_superuser:
        users = User.objects.all()
        context["users"] = users
    if request.user.is_authenticated:
        context["logout"] = "logout"

    return render(request, "home.html", context)

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data["firstname"]
        lastname = form.cleaned_data["lastname"]
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirm_password = form.cleaned_data["confirm_password"]


        if password == confirm_password:
            if strongPassword(password):
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Taken")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    return redirect("accounts:login")
            else:
                messages.info(request, "Password is not strong")
                print(password)
    context = {
        "form" : form
    }

    return render(request, "signup.html", context)
def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Incorrect username or password")
    context = {
        "form" : form
    }
    return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect("accounts:login")

def userEdit(request, id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    obj = User.objects.get(id=id)
    initial_data = {
        "firstname" : obj.first_name,
        "lastname" : obj.last_name,
        "username" : obj.username,
        "email" : obj.email,
        "password" : obj.password
    }
    form = Userform(data=request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("home")
    context = {
        "form" : form
    }
    return render(request, "userEdit.html", context)

def userDelete(request, id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect("accounts:login")
    context = {
        "user" : user
    }
    return render(request, "userDelete.html", context)

def strongPassword(password):
    lowercasePattern = re.compile(r"[a-z]")   #compile to check for lower case
    uppercasePattern = re.compile(r"[A-Z]")               #compile to check for uppercase
    digitPattern = re.compile(r"[0-9]")               #compile to check for digits

    lowercasePatternCheck = lowercasePattern.findall(password)
    uppercasePatternCheck = uppercasePattern.findall(password)
    digitPatternCheck = digitPattern.findall(password)

    passwordPattern = "".join(lowercasePatternCheck+uppercasePatternCheck+digitPatternCheck)

    if len(passwordPattern) >= 8:
            if lowercasePatternCheck and uppercasePatternCheck and digitPatternCheck:
                return True
            else:
                return False   