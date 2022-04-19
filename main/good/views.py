from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioForm
from reviews.decorators import allowed_users

# Create your views here.


def home(request):
    information = Portfolio.objects.all()
    context = {'information': information}
    return render(request, 'good/home.html', context)


@login_required(login_url='login')
def userform(request):
    form = PortfolioForm()

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'good/userform.html', context)


@login_required(login_url='login')
def updatepage(request, pk):
    useit = Portfolio.objects.get(id=pk)
    form = PortfolioForm(instance=useit)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=useit)
        if form.is_valid():
            form.save()
            return redirect('users')

    context = {'form': form}
    return render(request, 'good/updatepage.html', context)


@login_required(login_url='login')
def currentusers(request, pk):
    info = Portfolio.objects.filter(id=pk)
    context = {'info': info}
    return render(request, 'good/currentusers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def users(request):
    info = Portfolio.objects.all()
    context = {'info': info}
    return render(request, 'good/users.html', context)


def stylepage(request):
    return render(request, 'good/stylepage.html')
