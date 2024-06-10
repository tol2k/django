from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    template = 'catalog.html'
    if sort == 'min_price':
        sort = 'price'
    elif sort == 'max_price':
        sort = '-price'
    context = {'phones': Phone.objects.all().order_by(sort)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)

