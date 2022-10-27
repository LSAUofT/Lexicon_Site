from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "Home.html")  # these file paths may need to be different


def about(request):
    return render(request, "About.html")  # these file paths may need to be different


def contact(request):
    return render(request, "Contact.html")  # these file paths may need to be different
