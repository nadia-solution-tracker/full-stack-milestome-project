from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from bookstore.settings import MEDIA_URL
from reviews.forms import ReviewForm
from reviews.models import Review
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat

# Reference- https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def all_products(request):
    """List of all books in the database with pagination"""
    products = Product.objects.all().order_by('name')
    # products_list  = Product.objects.get_queryset()
    category = Category.objects.all()
    best_seller_books = Product.objects.raw("select * from products_product where instock<=1 order by instock limit 10")
 
   
    #Reference https://tutorial.djangogirls.org/en/django_orm/
    sorting_order =  request.GET.get('sort-by-price')
    
    if request.GET.getlist('sort-by-price'):
        if 'Low-to-High' in request.GET.getlist('sort-by-price'):
            products  = products.order_by('price')
        if 'High-to-Low' in request.GET.getlist('sort-by-price'):
            products  = products.order_by('-price')
            
   
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
  
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    context = {"products":products,
                "category":category, 
                "best_seller_books":best_seller_books, 
                "sorting_order" : sorting_order}
    
    return render(request,"product_list.html", context)

# Reference -https://www.codementor.io/jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a
def product_detail(request,id):
    """Specific details of a particular book"""
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
    """Displays categories for each book"""
    category = Category.objects.all()
    best_seller_books = Product.objects.raw("select * from products_product where instock<=1 order by instock limit 10")
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
        "best_seller_books" : best_seller_books,
        "MEDIA_URL": MEDIA_URL, 
    })
    

