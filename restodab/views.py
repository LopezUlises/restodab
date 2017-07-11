from django.shortcuts import render
from .models import Consumicion


def guarnicion_list(request):
    convar = Consumicion.objects.all().filter(categoria="G").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})

def bebidas_list(request):
    convar = Consumicion.objects.all().filter(categoria="B").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})
