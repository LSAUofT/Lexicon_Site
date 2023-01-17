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

            # send_mail(
            #     'Lex. Sci. Asia: Message Received',  # subject
            #     form.cleaned_data['user_message'],  # email message
            #     None,  # email that this message from -- b/c None, sent from default email (defined in settings)
            #     ['lexscieasia@gmail.com'],  # email this is getting sent to (can have more than one)
            #     fail_silently=False,
            # )

            # redirect to a new URL:
            # this is going to try to send user to page with URL /thanks/ -- absolute path
            # currently, WILL cause errors, something's up with the URLs
            return HttpResponseRedirect('thanks/')  # this will take you to the associated URL

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        # # renders form according to the formatting described in nice_form.html
        # rendered_form = form.render("base/nice_form.html")
        # context = {'form': rendered_form}
        print("SECOND IF HERE")

    # return render(request, "base/Contact.html", context)  # sends form information to be rendered
    return render(request, "base/Contact.html", {'form': form})


def news(request):
    return render(request, "base/News.html")


def thanks(request):
    return render(request, "base/Thanks.html")
