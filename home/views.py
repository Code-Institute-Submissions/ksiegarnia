from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    """ A view for the index page """

    products = Product.objects.filter(genre='1')[:3]
    newest_products = Product.objects.order_by('-pub_date')[:4]



    context = {
        'products': products,
        'newest_products': newest_products,

    }

    return render(request, 'home/index.html', context)


def newest(request):
    """ A page  showing the last 12 books added"""

    newest_products = Product.objects.order_by('-pub_date')[:11]
    context = {

        'newest_products': newest_products,

    }


    return render(request, 'home/newest.html', context)