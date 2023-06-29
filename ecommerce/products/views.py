from django.shortcuts import render

# Create your views here.


def getProduct(request, slug):
    return render(request, 'product/product.html')
