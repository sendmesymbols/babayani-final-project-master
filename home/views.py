from django.shortcuts import render
from products.models import *
# Create your views here.


def index(request):
    """ Return to index page """

    products = Top_selling_product.objects.all()
    context = {'products':products}

    return render(request, 'home/index.html',context)
    