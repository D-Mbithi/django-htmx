from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()[:8]

    context = {
        'products': products
    }

    return render(request, 'shop/home.html', context)
