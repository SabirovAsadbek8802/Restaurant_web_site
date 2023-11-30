from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Accounts


def registration(request):
    return render(request, "register.html")


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name'):
            person = Accounts()
            person.username = request.POST.get('username')
            person.email = request.POST.get('email')
            person.password = request.POST.get('password')
            person.save()
            return render(request, 'register.html')

    else:
        return render(request, 'login.html')
