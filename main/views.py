from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import *

import numpy as np

@login_required()
def index(request):
    category = Category.objects.all()
    return render(request, "index.html", {
        'category': category,
        'products': Product.objects.all()
    })


@login_required()
def about(request):
    return render(request, "about.html")


@login_required()
def blog(request):
    return render(request, "blog.html")


@login_required()
def cart(request):
    return render(request, "cart.html")


@login_required()
def blog_details(request):
    return render(request, 'blog-details.html')


@login_required()
def checkout(request):
    return render(request, "checkout.html")


@login_required()
def contact(request):
    return render(request, "contact.html")


@login_required()
def faq(request):
    return render(request, "faq.html")


@login_required()
def history(request):
    return render(request, "history.html")


@login_required()
def menu(request):
    return render(request, "menu.html")


@login_required()
def reservation(request):
    return render(request, "reservation.html")


@login_required()
def shop_details(request, name):
    product_detail = ProductDetail.objects.filter(products__name=name).all()
    product = Product.objects.filter(name=name).first()
    products = Product.objects.all()
    random_products = np.random.choice(products, 3, replace=False)

    product_info = ProductInfo.objects.filter(products__name=name).all()
    product_description = ProductDetail.objects.filter(products__name=name).all()

    reviews = ProductReview.objects.filter(products__name=name).all()

    return render(request, "shop-details.html", {
        'product_details': product_detail,
        'product': product,
        'products': random_products,
        'infos': product_info,
        'descriptions': product_description,
        'reviews': reviews,
    })


@login_required()
def shop_sidebar(request):
    product = Product.objects.all()
    return render(request, "shop-sidebar.html", {
        'product': product,
    })


@login_required()
def shop(request):
    item = Product.objects.all()
    return render(request, "shop.html", {
        'products':item
    })


@login_required()
def team(request):
    return render(request, "team.html")
