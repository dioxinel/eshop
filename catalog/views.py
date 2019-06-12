from django.shortcuts import render
from .models import *
# Create your views here.

def catalog_list(request):
    sections = Section.objects.all()
    return render(request, 'catalog/catalog_list.html', context={'sections':sections})

def section_detail(request, id):
    section = Section.objects.get(id__iexact=id)
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', context={'section':section, 'categories':categories})
