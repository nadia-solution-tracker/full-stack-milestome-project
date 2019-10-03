from django.shortcuts import render,  get_object_or_404
from products.models import Product
from .forms import ReviewForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return render(request, 'add_review.html', {'form': form})
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})
