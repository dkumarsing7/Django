from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'this is sent',
    }
    return render(request,'index.html')
    # return HttpResponse("Hello, World!")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is aboutpage")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services")
def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("this is contact")
    