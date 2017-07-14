from django.shortcuts import render, get_object_or_404
from .models import Consumicion


def pagprincipal(request):
    return render(request, 'pagina1.html')

def guarnicion_list(request):
    convar = Consumicion.objects.all().filter(categoria="G").order_by('nombre')
    P = "Guarniciones"
    return render(request, 'lista.html', {'consumicion': convar, 'titulo' : P})

def bebidas_list(request):
    convar = Consumicion.objects.all().filter(categoria="B").order_by('nombre')
    P = "Bebidas"
    return render(request, 'lista.html', {'consumicion': convar, 'titulo' : P})

def postre_list(request):
    convar = Consumicion.objects.all().filter(categoria="P").order_by('nombre')
    P = "Postres"
    return render(request, 'lista.html', {'consumicion': convar, 'titulo' : P})

def lunch_list(request):
    convar = Consumicion.objects.all().filter(categoria="L").order_by('nombre')
    P = "Lunch's"
    return render(request, 'lista.html', {'consumicion': convar, 'titulo' : P})

def breakfast_list(request):
    convar = Consumicion.objects.all().filter(categoria="D").order_by('nombre')
    P = "Desayunos"
    return render(request, 'lista.html', {'consumicion': convar, 'titulo' : P})

def producto(request, pk):
        con = get_object_or_404(Consumicion, pk=pk)
        return render(request, 'produc.html', {'con': con})