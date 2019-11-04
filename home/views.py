from django.shortcuts import render
from products.models import Category,Product,Author
# Create your views here.

def home_page(request):
    """A view displays the Home Page"""
    category = Category.objects.all()
    best_seller_books = Product.objects.raw("select * from products_product where instock<=1 order by instock limit 10")
    top_3_product= Product.objects.raw("select * from products_product where views>=1 order by views desc limit 3")
    context = {
        "top_3_product":  top_3_product,
        "category" :category,
        "best_seller_books" : best_seller_books
    }
    return render(request,'home_page.html',context)
