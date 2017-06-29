from django.shortcuts import render
from .models import Bebida
from .models import Lanch

# Create your views here.
def post_list(request):
    bebidasvar = Bebida.objects.all()
    return render(request, 'pagina1.html', {'bebidas': bebidasvar})

def listar_bebida(request):
    bebidasvar = Bebida.objects.all()
    return render(request, 'pagbeb.html', {'bebidas': bebidasvar})

def listar_lanch(request):
    lanchvar = Lanch.objects.all()
    return render(request, 'paglan.html', {'lanch': lanchvar})
