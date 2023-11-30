from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")
def cart(request):
    return render(request, "cart.html")


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def history(request):
    return render(request, "history.html")


def menu(request):
    return render(request, "menu.html")


def reservation(request):
    return render(request, "reservation.html")


def shop_details(request):
    return render(request, "shop-details.html")


def shop_sidebar(request):
    return render(request, "shop-sidebar.html")


def shop(request):
    return render(request, "shop.html")


def team(request):
    return render(request, "team.html")
