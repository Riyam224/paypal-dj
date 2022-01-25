from importlib import import_module
from django.urls import path 
from . import views 


app_name = 'product'

urlpatterns = [
    path('' , views.index , name='index'),
    path('<int:id>/' , views.product_detail , name='product_detail'),
]
