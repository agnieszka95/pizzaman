from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Product2
from .forms import OrderForm
from hello.models import Order

# Create your views here.
def index(request):
    return render(request, 'index.html', {'pizza_list': Product2.objects.all()})

def thank(request):
    return render(request, 'thank.html')

def products(request):
    return render(request, 'products.html')

def createOrder(form, product):
    order =  Order(name=form.cleaned_data['customerName'],surname=form.cleaned_data['customerSurname'], postalcode=form.cleaned_data['customerPostalCode'],
                   city=form.cleaned_data['customerCity'], street=form.cleaned_data['customerStreet'], email=form.cleaned_data['customerEmail'], product=product)
    order.save()

def checkout(request, id):
    # if this is a POST request we need to process the form data
    instance = get_object_or_404(Product2, id=id)
    Context = {
        "id": instance.id,
        "instance": instance
    }
    product = Product2.objects.get(id=id)


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)

    # check whether it's valid:
        if form.is_valid():
            createOrder(form, product)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thank/')
        # else
        #     #przkazujemy forma i errory
        #     f.['message'].errors

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form, 'instance': Context})