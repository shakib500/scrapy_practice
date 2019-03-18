from django.shortcuts import render, HttpResponse

#from django.views.generic import ListView, DetailView


from .models import Product 




def index(request):
    products = Product.objects.all()
    return render(request, "product/list.html",{'object_list':products})