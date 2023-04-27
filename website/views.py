from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
#from .forms import ApplicationForm
#from .models import Form

#from . import tags

# Create your views here.
def index(request):

    return render(request, "index.html", {})

# resume page
def resume(request):
    return render(request, "resume.html", {})

# filmtv page
def filmtv(request):
    return render(request, "filmtv.html", {})

# about page
def about(request):
    return render(request, "about.html", {})

# contact page
def contact(request):
    return render(request, "contact.html", {})

# jobapp page
def jobapp(request):
    if request.method == "POST":
        # show success message
        messages.success(request, "Form submitted successfully", {})


    return render(request, "jobapp.html")
