from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from bookstore.settings import MEDIA_URL
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.
def all_products(request):
    products_list = Product.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request,"product_list.html",{"products":products,"category":category, "author":author})


def product_detail(request,id):
    product= get_object_or_404(Product, id=id)
    reviews = Review.objects.filter(product_id=id).order_by('pub_date')
    product.views = product.views + 1
    product.save()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ReviewForm()
    
      
    context={
        'product': product,
        'reviews' : reviews,
        'form': form
    }
    return render(request,'product_detail.html',context)
    
def show_products_category(request, category_name):
    category = Category.objects.all()
    author = Author.objects.all()
    category_select = Category.objects.get(name=category_name)
    product_pagination = Product.objects.filter(category = category_select).order_by('name')
    page = request.GET.get('page', 1)
    paginator = Paginator(product_pagination , 3)
    try:
        products= paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return render(request, "product_list.html",
    {
        "products": products, 
        "category_name": category_name, 
        "category" : category,
        "author" : author,
        "MEDIA_URL": MEDIA_URL, 
    })
    
# def show_products_author(request, author_firstname,author_lastname):
#     author = Author.objects.all()
#     author_select = Author.objects.get(firstname=author_firstname, lastname=author_lastname)
#     product_pagination = Product.objects.filter(author = author_select).order_by('firstname')
#     page = request.GET.get('page', 1)
#     paginator = Paginator(product_pagination , 3)
#     try:
#         products= paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
        
#     return render(request, "product_list.html",
#     {
#         "products": products, 
#         "author_firstname": author_firstname, 
#         "author_lastname": author_lastname,
#         "MEDIA_URL": MEDIA_URL, 
#     })
    
