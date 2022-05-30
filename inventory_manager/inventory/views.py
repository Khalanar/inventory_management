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
        
        form_data = {
            'name': request.POST['name'],
            'sku': request.POST['sku'],
            'status': request.POST['status'],
            'stock': request.POST['stock'],
            'price': request.POST['price'],
            'description': request.POST['description'],
        }
        
        new_product_form = NewProductForm(form_data)

        if new_product_form.is_valid():
            print('form is valid')
            product = new_product_form.save(commit=False)
            product.save()
            print('saved product')

    else:
        new_product_form = NewProductForm()

    context = {
        'new_product_form': new_product_form,
    }

    return render(request, 'inventory/create_product.html', context)