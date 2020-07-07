from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', context={'products': products})


def new(request):
    return HttpResponse("new product")
