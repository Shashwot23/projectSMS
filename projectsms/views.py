from django.shortcuts import render, redirect
from product.models import Product
from accounts.forms import SignupForm
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
import random

def landingPage(request):
    product_data=Product.objects.all()[:8]
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart

    data={
        'product_data':product_data
    }
    return render(request, 'index.html', data)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('landing')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form':form})

def product(request):
    product_data=Product.objects.all()
    if request.method=="GET":
        search_product = request.GET.get("search_product")
        if search_product!=None:
            product_data=Product.objects.filter(product_name__icontains=search_product)


    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
    data={
        'product_data':product_data
    }
    return render(request, 'product.html',data)


def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price += product.product_price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    
    data = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', data)


def update_cart(request):
    product_id = request.POST.get('product_id')
    action = request.POST.get('action')

    cart = request.session.get('cart', {})
    quantity = cart.get(product_id, 0)

    if action == 'increase':
        cart[product_id] = quantity + 1
    elif action == 'decrease' and quantity > 1:
        cart[product_id] = quantity - 1
    else:
        del cart[product_id]

    request.session['cart'] = cart
    return HttpResponseRedirect('/cart/')


def product_details(request,slug):
    product_details=Product.objects.get(product_slug=slug)
    related_products = Product.objects.order_by('?').exclude(product_slug=slug)[:4]


    data={
        'product_details':product_details,
        'related_products':related_products
        }
    return render(request, 'product_details.html', data )
