from django.shortcuts import render, HttpResponse
from datetime import datetime as date
from Home.models import Contact
# Create your views here.
def index(request): 
    return render(request,'index.html')
    # return HttpResponse("Hello, World!")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is aboutpage")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date.today())
            contact.save()
            print("Contact saved successfully!")
        else:
            print("Missing form data")

    return render(request, 'contact.html')
