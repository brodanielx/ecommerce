from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import ContactForm, LoginForm

def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'home_page.html', {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title' : "Contact",
        'content': 'Welcome to the contact page',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated())
            print(user)
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            print('error')
    return render(request, 'auth/login.html', context)







def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'auth/register.html', context)
