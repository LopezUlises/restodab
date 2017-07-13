from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.pagprincipal),
        url(r'^bebida/$', views.bebidas_list),
        url(r'^postre/$', views.postre_list),
        url(r'^guarnicion/$', views.guarnicion_list),
        url(r'^lunch/$', views.lunch_list),
        url(r'^breakfast/$', views.breakfast_list),
]
