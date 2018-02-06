from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'home_page.html', {})

def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title' : "Contact",
        'content': 'Welcome to the contact page',
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)
