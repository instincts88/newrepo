from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello!</h1>")
# Create your views here.
def viewform(request):
    return HttpResponse("<h1>Check this out</h1>")