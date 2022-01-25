import json
from django.shortcuts import render , get_object_or_404

# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from .models import Product ,  Order


def index(request):
    return HttpResponse('home ')


def product_detail(request , id):
    product = get_object_or_404(Product , id=id)
    context = {
        'product': product 
    }
    return render(request , 'product/detail.html', context)


def order_completed(request):
    body = json.loads(request.body)
    product = Product.objects.get(id=body['product_id'])

    Order.objects.create(
         product = product,
         order_id = 122991,
         order_completed  = True
    )
    
    return JsonResponse('Payment completed ! ')