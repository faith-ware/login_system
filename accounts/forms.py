from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={
        "name" : "username",
        "type" : "text",
        "placeholder" : "Enter your username"
    }))

    password = forms.CharField(label="Password",widget=forms.TextInput(attrs={
        "name" : "password",
        "type" : "password",
        "placeholder" : "Enter your password"
    }))
    
class SignupForm(forms.Form):
    firstname = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
        "name" : "firstname",
        "placeholder" : "Enter your first name",
        "required" : "required",
    }))

    lastname = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
        "name" : "lastname",
        "placeholder" : "Enter your last name",
        "required" : "required",
    }))

    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={
        "name" : "username",
        "required" : "required",
        "type" : "text",
        "placeholder" : "Enter your username"
    }))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
        "name" : "email",
        "required" : "required",
        "type" : "email",
        "placeholder" : "Enter your email",
    }))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "name" : "password",
        "required" : "required",
        "type" : "password",
        "placeholder" : "Enter your password",
    }))

    confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={
        "name" : "confirm_password",
        "required" : "required",
        "type" : "password",
        "placeholder" : "Confirm your password",
    }))

class Userform(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
        "name" : "firstname",
        "placeholder" : "Enter your first name",
        "required" : "required",
    }))

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
        "name" : "lastname",
        "placeholder" : "Enter your last name",
        "required" : "required",
    }))

    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={
        "name" : "username",
        "required" : "required",
        "type" : "text",
        "placeholder" : "Enter your username"
    }))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
        "name" : "email",
        "required" : "required",
        "type" : "email",
        "placeholder" : "Enter your email",
    }))

    is_staff= forms.BooleanField(required=False,label="Staff",widget=forms.CheckboxInput(attrs={
    }))

    is_active= forms.BooleanField(required=False,label="Active",widget=forms.CheckboxInput(attrs={

    }))
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email","is_staff", "is_active"]
