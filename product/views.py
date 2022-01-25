from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Product ,  Order


def index(request):
    return HttpResponse('home ')


def product_detail(request , id):
    product = get_object_or_404(Product , id=id)
    context = {
        'product': product 
    }
    return render(request , 'product/detail.html', context)
