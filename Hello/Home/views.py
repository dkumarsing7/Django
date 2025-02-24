from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'this is sent',
    }
    return render(request,'index.html', context)
    # return HttpResponse("Hello, World!")
def about(request):
    return HttpResponse("this is aboutpage")
def services(request):
    return HttpResponse("this is services")
def contact(request):
    return HttpResponse("this is contact")
    