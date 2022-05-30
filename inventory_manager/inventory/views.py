from django.shortcuts import render
from .models import Product, Status

from .forms import NewProductForm

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

def create_product(request):

    if request.method == "POST":
        print('POST FORM')
    else:
        new_product_form = NewProductForm()

        context = {
            'new_product_form': new_product_form,
        }

    return render(request, 'inventory/create_product.html', context)