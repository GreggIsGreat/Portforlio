from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm,registerForm
from django.contrib.auth.models import Group


# Create your views here.


def index(request):
    return render(request, 'cap/index.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password incorrect!')
    else:
        form = AuthenticationForm()

    return render(request, 'cap/index.html', context={'form': form})


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            group = Group.objects.get(name='Student')
            user.groups.add(group)
            login(request, user)
            return redirect('userform')
        messages.success(request, 'You have successfully logged in!')

    context = {'page': page, 'form': form}
    return render(request, 'cap/index.html', context)

def registerad(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            group = Group.objects.get(name='Admin')
            user.groups.add(group)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = registerForm()
    return render(request, 'cap/registerad.html', {'form': form})