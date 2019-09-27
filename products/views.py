from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all_products(request):
    products_list = Product.objects.all()
    category = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request,"product_list.html",{"products":products,"category":category})


def product_detail(request,id):
    product= get_object_or_404(Product, id=id)

    context={
        'product': product,
    }
    return render(request,'product_detail.html',context)