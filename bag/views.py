from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view for showing shopping cart page """

    return render(request, 'bag/bag.html')