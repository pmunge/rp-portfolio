# pages/views.py

from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')