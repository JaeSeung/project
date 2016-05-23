from django.shortcuts import render
from .models import Product



def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/detail.html', {
    'product_list':product_list})

def get_products(request, next_pk):
    '''return the products from pk to pk+100'''
    nid = int(next_pk)
    products = Product.objects.order_by('-pk')[nid:nid+3]
    if request.is_ajax():
        return render(request, 'product/product.ajax.html', {'next_pk': nid+3, 'products': products})
    else:
        return render(request, 'product/view_products.html', {'next_pk': nid+3, 'products': products})

# Create your views here.
