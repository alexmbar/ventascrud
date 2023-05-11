from django.shortcuts import render
from .models import Productos

# Create your views here.
def productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html',{
        'productos': productos
    } )