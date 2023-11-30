from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("blog/", blog, name='blog'),
    path("blog/d/", blog_details, name='blog-details'),
    path("checkout/", checkout, name='checkout'),
    path("contact/", contact, name='contact'),
    path("history/", history, name='history'),
    path("faq/", faq, name='faq'),
    path("cart/", cart, name='cart'),
    path("menu/", menu, name='menu'),
    path("reservation/", reservation, name='reservation'),
    path("shop-details/", shop_details, name='shop-details'),
    path("shop-sidebar/", shop_sidebar, name='shop-sidebar'),
    path("shop/", shop, name='shop'),
    path("team/", team, name='team'),
    path("login/", login, name='login'),
    path("register/", register, name='register'),
    path("forgot-password/", forgot_password, name='forgot-password'),
]

