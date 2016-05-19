from django.shortcuts import render
from .models import Product


def intro(request):
    return render(request, 'product/intro.html')


def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/detail.html', {
    'product_list':product_list})

# Create your views here.
