from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from good.models import Portfolio
from .forms import ReviewForm
from .decorators import allowed_users


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def reviews(request):
    tap = Review.objects.all()
    context = {'tap': tap}
    return render(request, 'reviews/reviews.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def reviewform(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews')

    context = {'form': form}
    return render(request, 'reviews/reviewform.html', context)


@login_required(login_url='login')
def deletereview(request, pk):
    lint= Review.objects.get(id=pk)
    if request.method == 'POST':
        lint.delete()
        return redirect('reviews')

    context = {'lint': lint}
    return render(request, 'reviews/deletereview.html', context)
