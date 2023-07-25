from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides' : nSlides, 'range' : range(1, nSlides), 'product' : products}
    params = {'product' : products}
    print(params)
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def search_product(request):
    return render(request, 'shop/search.html')

def single_product(request):
    return HttpResponse("This is single product Page")

def checkout(request):
    return HttpResponse("This is checkout Page")

def tracking(request):
    return HttpResponse("This is tracking Page")