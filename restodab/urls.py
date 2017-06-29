from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url (r'^bebida/$', views.listar_bebida),
        url (r'^lanch/$', views.listar_lanch),
]



