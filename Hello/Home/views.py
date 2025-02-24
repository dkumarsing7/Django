from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
def about(request):
    return HttpResponse("this is aboutpage")
def services(request):
    return HttpResponse("this is services")
def contact(request):
    return HttpResponse("this is contact")
    