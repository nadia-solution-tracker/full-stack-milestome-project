from django.shortcuts import render
from products.models import Product, Category, Author
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def search_products(request):
    """Search for a particular book ,author or specific keywords"""
    product_list = Product.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    query = request.GET.get('q')
    if query:
     
        product_list = Product.objects.filter(
            Q(name__icontains=query) | Q(author__firstname__icontains=query) | Q(author__lastname__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
        ).distinct()
    page = request.GET.get('page',1)
    paginator = Paginator(product_list, 6)
   

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'category':category,
        'author': author
    }

 
    return render(request, "product_list.html", context)