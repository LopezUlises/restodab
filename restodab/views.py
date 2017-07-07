from django.shortcuts import render
from .models import Bebida
from .models import Lanch
from .models import Postre
from .models import Guarnicion
from .models import Breackfast

def post_list(request):
    bebidasvar = Bebida.objects.all().order_by('nombre')
    return render(request, 'pagina1.html', {'bebidas': bebidasvar})

def listar_bebida(request):
    bebidasvar = Bebida.objects.all()
    return render(request, 'pagbeb.html', {'bebidas': bebidasvar})

def listar_lanch(request):
    lanchvar = Lanch.objects.all()
    return render(request, 'paglan.html', {'lanch': lanchvar})

def listar_postre(request):
    postrevar = Postre.objects.all()
    return render(request, 'pagpostre.html', {'postre': postrevar})

def listar_guarnicion(request):
    guarnicionvar = Guarnicion.objects.all()
    return render(request, 'pagguar.html', {'guarnicion': guarnicionvar})

def listar_breackfast(request):
    breackvar = Breackfast.objects.all()
    return render(request, 'pagbreack.html', {'breack': breackvar})
