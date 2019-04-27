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
    	price_list = Product.objects.values_list('price', flat=True).filter(Q(name__icontains=query))
    	find_num = []
    	for prod_price in price_list:
    		find_num_temp = [n for n in re.findall(r'(\d+)',prod_price.replace(',',''))]
    		y = ''.join(find_num_temp)
    		find_num.append(int(y))
    	find_num.sort()
    	print(find_num)
    	return render(request, "product/list.html",{'object_list':results})

