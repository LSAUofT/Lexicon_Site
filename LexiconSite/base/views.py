from django.shortcuts import render
from django.http import HttpResponse

# TODO: Update the html file names


def home(request):
    return render(request, "base/Home.html")

def about(request):
    return render(request, "base/About.html")

def about_project(request):
    return render(request, "base/About-the-Project.html")

def about_team(request):
    return render(request, "base/About-the-Team.html")

def technical_information(request):
    return render(request, "base/Technical-Information.html")

def contact(request):
    return render(request, "base/Contact.html")

def news(request):
    return render(request, "base/News.html")