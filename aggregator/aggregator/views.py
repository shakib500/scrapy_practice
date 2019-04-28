from django.shortcuts import render, HttpResponse

from product.models import Product 
from django.db.models import Q
import re

def index(request):
    query = request.GET.get('q')
    if query == None:
    	return render(request, "index.html")

    else:
    	results = Product.objects.filter(Q(name__icontains=query))
    	return render(request, "product/list.html",{'object_list':results})

