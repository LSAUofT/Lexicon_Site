from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # TODO: include code here to actually send the email
            #  (link: https://docs.djangoproject.com/en/4.1/topics/email/)

            # redirect to a new URL:
            # this is going to try to send user to page with URL /thanks/ -- absolute path
            # this doesn't currently appear to...do...anything?
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # else:
        # form = ContactForm()
        # # renders form according to the formatting described in nice_form.html
        # rendered_form = form.render("base/nice_form.html")
        # context = {'form': rendered_form}

    # return render(request, "base/Contact.html", context)  # sends form information to be rendered
    return render(request, "base/Contact.html")

def news(request):
    return render(request, "base/News.html")
