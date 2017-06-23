from django.contrib import admin

# Register your models here.
from .models import Bebida
from .models import Lanch
from .models import Postre
from .models import Guarnicion
from .models import Breackfast

admin.site.register(Bebida)
admin.site.register(Lanch)
admin.site.register(Postre)
admin.site.register(Guarnicion)
admin.site.register(Breackfast)