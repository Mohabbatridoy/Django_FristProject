from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Homepage!</h1> <a href='contact/'>Contact</a> <a href='about/'>about</a>")
def contact(request):
    return HttpResponse("this is contact page <a href='/'>Home</a> <a href='/about/'>About us</a>")

def about(request):
    return HttpResponse("this is aboutpage <a href='/'>Home</a> <a href='/contact/'>Contact</a>")