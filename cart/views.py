from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product

# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    updated_stock = product.instock
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    request.session['cart'] = cart
    for k, v in cart.items():
        if k == id:
            updated_stock -= v
            if updated_stock == 0 and id in cart:
                update = Product.objects.filter(id = id).update(instock = updated_stock)
    return redirect(reverse('products'))
    
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart',{})
    updated_stock = product.instock
    if quantity > 0:
        cart[id] = quantity
        for k,v in cart.items():
            if k == id:
                updated_stock -= v
                if updated_stock == 0:
                    update = Product.objects.filter(id = id).update(instock = updated_stock)
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def remove_from_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    updated_stock = product.instock
    update = Product.objects.filter(id = id).update(instock = updated_stock)
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    