from django.shortcuts import render, HttpResponse

from .models import Product 
from django.db.models import Q
import re

def index(request):
    query = request.GET.get('q')
    if query == None:
    	products = Product.objects.all()
    	return render(request, "product/list.html",{'object_list':products})
    else:
    	results = Product.objects.filter(Q(name__icontains=query))
    	return render(request, "product/list.html",{'object_list':results})

