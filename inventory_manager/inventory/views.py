from django.shortcuts import render
from .models import Product, Status

# Create your views here.

def index(request):
    """View to load index page"""

    status = Status.objects.all()
    products = Product.objects.all()

    context = {
        'status': status,
        'products': products,
    }

    return render(request, 'inventory/index.html', context)