from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))


    # allprods = []
    # products_Catagories = Product.objects.values('category', 'id')
    # cats = {item['category'] for item in products_Catagories}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     allprods.append([prod, range(1, nSlides), nSlides])


    params = {'no_of_slides' : nSlides, 'range':range(1, nSlides), 'products':products}
    # print(params)
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