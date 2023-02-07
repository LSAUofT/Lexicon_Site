from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail

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
    print(request.method)

    if request.method == 'POST':
        form = ContactForm(request.POST)  # create a form instance and populate it with data from the request:
        if form.is_valid():
            # process the data in form.cleaned_data (a dict) as required
            print(form.cleaned_data)

            send_mail(
                'Lex. Sci. Asia: Message Received',  # subject
                form.cleaned_data['user_message'],  # email message
                None,  # email that this message from -- b/c None, sent from default email (defined in settings)
                ['lexsciasia@gmail.com'],  # email this is getting sent to (can have more than one)
                fail_silently=False,
            )

            # redirect to a new URL (relative to current page):
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        print("SECOND IF HERE")

    return render(request, "base/Contact.html", {'form': form})


def news(request):
    return render(request, "base/News.html")


def thanks(request):
    return render(request, "base/Thanks.html")


def lexicon(request):
    return render(request, "base/Lexicon.html")
