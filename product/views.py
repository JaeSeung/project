from django.shortcuts import render



def intro(request):
    return render(request, 'product/intro.html')
def product_list(request):
    return render(request, 'product/detail.html')

# Create your views here.
