from django.shortcuts import render
from .models import Consumicion


def pagprincipal(request):
    return render(request, 'pagina1.html')

def guarnicion_list(request):
    convar = Consumicion.objects.all().filter(categoria="G").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})

def bebidas_list(request):
    convar = Consumicion.objects.all().filter(categoria="B").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})

def postre_list(request):
    convar = Consumicion.objects.all().filter(categoria="P").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})

def lunch_list(request):
    convar = Consumicion.objects.all().filter(categoria="L").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})

def breakfast_list(request):
    convar = Consumicion.objects.all().filter(categoria="D").order_by('nombre')
    return render(request, 'lista.html', {'consumicion': convar})
