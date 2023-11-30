from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")


@login_required(login_url='/login')
def about(request):
    return render(request, "about.html")


@login_required(login_url='/login')
def blog(request):
    return render(request, "blog.html")


@login_required(login_url='/login')
def cart(request):
    return render(request, "cart.html")


@login_required(login_url='/login')
def blog_details(request):
    return render(request, 'blog-details.html')


@login_required(login_url='/login')
def checkout(request):
    return render(request, "checkout.html")


@login_required(login_url='/login')
def contact(request):
    return render(request, "contact.html")


@login_required(login_url='/login')
def faq(request):
    return render(request, "faq.html")


@login_required(login_url='/login')
def history(request):
    return render(request, "history.html")


@login_required(login_url='/login')
def menu(request):
    return render(request, "menu.html")


@login_required(login_url='/login')
def reservation(request):
    return render(request, "reservation.html")


@login_required(login_url='/login')
def shop_details(request):
    return render(request, "shop-details.html")


@login_required(login_url='/login')
def shop_sidebar(request):
    return render(request, "shop-sidebar.html")


@login_required(login_url='/login')
def shop(request):
    return render(request, "shop.html")


@login_required(login_url='/login')
def team(request):
    return render(request, "team.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def forgot_password(request):
    return render(request, "forgot-password.html")
