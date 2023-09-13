# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Person





def index(request):
    context = {}
    return render(request, 'index.html', context)

# def login(request):
#     context = {}
#     return render(request, 'login.html', context)

# def register(request):
#     context = {}
#     return render(request, 'register.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'forgot_password.html', context)

def tables(request):
    context = {}
    return render(request, 'tables.html', context)

def charts(request):
    context = {}
    return render(request, 'charts.html', context)

def error_404(request):
    context = {}
    return render(request, 'error_404.html', context)

from django.contrib import messages
@login_required
# @user_passes_test(is_admin)
def blank(request):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to access this page. Please login as admin")
        return redirect('login')  # Replace 'error_404' with the appropriate URL or view name for your error page

    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'blank.html', context)

from .forms import PersonForm
@login_required
def update_person(request):
    try:
        person = request.user.person
    except:
        person = Person(user=request.user)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Assuming you have a profile view to display the person's profile
    else:
        form = PersonForm(instance=person)

    return render(request, 'profile.html', {'form': form})

def send_login_email(username):
    from postmarker.core import PostmarkClient
    from django.utils import timezone

    try:
        postmark = PostmarkClient(server_token='API-TOKEN')
        postmark.emails.send(
            From='info@email.com',
            To='info@email.com',
            Subject='Postmark test',
            HtmlBody=f'The user {username} logged in at {timezone.now()}'
        )
        print("Login email sent")
    except postmarker.core.PostmarkException as e:
        print("Failed to send login email:", str(e))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            send_login_email(username)
            return redirect('index')  # Replace 'home' with the name of your home page URL
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Replace 'index' with the name of your home page URL

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace 'login' with the name of your login page URL
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

from rest_framework import generics
from .serializers import PersonSerializer

class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def vue_api(request):
    context = {}
    return render(request, 'vue_api.html', context)
