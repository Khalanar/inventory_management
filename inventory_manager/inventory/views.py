from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
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
        
        new_product_form = NewProductForm(request.POST)

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

def edit_product(request, id):
    print(id)
    if request.method == "POST":
        print(f'{id} - ID')
        product = Product.objects.get(id=id)
        new_product_form = NewProductForm(request.POST)

        if new_product_form.is_valid():
            product.name = new_product_form.cleaned_data['name']
            product.sku = new_product_form.cleaned_data['sku']
            product.status = new_product_form.cleaned_data['status']
            product.stock = new_product_form.cleaned_data['stock']
            product.price = new_product_form.cleaned_data['price']
            product.description = new_product_form.cleaned_data['description']
            product.save()

            return HttpResponseRedirect(reverse('inventory'))
    else:
        product = Product.objects.get(id=id)

        form_data = {
            'name': product.name,
            'sku': product.sku,
            'status': product.status,
            'stock': product.stock,
            'price': product.price,
            'description': product.description,
        }

        new_product_form = NewProductForm(form_data)

    context = {
        'new_product_form': new_product_form,
    }

    return render(request, 'inventory/edit_product.html', context)

def update_product_status(request, id, status_name):
    product = Product.objects.get(id=id)
    product.status = Status.objects.get(name=status_name)

    product.save()

    return HttpResponseRedirect(reverse('inventory'))

