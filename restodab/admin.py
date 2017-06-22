from django.contrib import admin

# Register your models here.
from .models import Comida
from .models import Bebida
from .models import Categoria

admin.site.register(Comida)
admin.site.register(Bebida)
admin.site.register(Categoria)
