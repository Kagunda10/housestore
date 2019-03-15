from django.shortcuts import render, get_object_or_404
from .models import Category, House
# Create your views here.

def house_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    houses = House.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        houses = houses.filter(category=category)
    return render(request,
                  'shop/house/list.html',
                  {'category': category,
                   'categories': categories,
                   'houses': houses})

def house_detail(request, id, slug):
    house = get_object_or_404(House,
                            id=id,
                            slug=slug,
                            available=True)
    return render(request,
                'shop/house/detail.html',
                {'house': house})