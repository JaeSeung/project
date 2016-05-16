from django.shortcuts import render



def intro(request):
    return render(request, 'product/intro.html')


# Create your views here.
