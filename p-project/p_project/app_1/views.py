from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    diction = {}
    return render(request, 'app_1/index.html',context=diction)