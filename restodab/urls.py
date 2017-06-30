from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url (r'^bebida/$', views.listar_bebida),
        url (r'^lanch/$', views.listar_lanch),
        url (r'^postre/$', views.listar_postre),
        url (r'^guarnicion/$', views.listar_guarnicion),
        url (r'^breackfast/$', views.listar_breackfast),
]



