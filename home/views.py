from django.shortcuts import render
from products.models import Category,Product,Author
# Create your views here.

def home_page(request):
    """A view displays the Home Page"""
    category = Category.objects.all()
    author = Author.objects.all()
    top_3_product= Product.objects.raw("select * from products_product where views>=1 order by views desc limit 3")
    context = {
        "top_3_product":  top_3_product,
        "category" :category,
        "author" : author
    }
    return render(request,'home_page.html',context)
