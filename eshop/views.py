from django.shortcuts import render

def a(request):
    a = 'Andriy'
    return render(request, 'eshop/index.html', context={'a':a})
# Create your views here.
