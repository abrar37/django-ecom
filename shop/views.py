from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def search_product(request):
    return HttpResponse("This is Search Page")

def single_product(request):
    return HttpResponse("This is single product Page")

def checkout(request):
    return HttpResponse("This is checkout Page")

def tracking(request):
    return HttpResponse("This is tracking Page")