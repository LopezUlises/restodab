from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.pagprincipal, name="restodab.views.pagprincipal"),
        url(r'^bebida/$', views.bebidas_list, name="restodab.views.bebidas_list"),
        url(r'^postre/$', views.postre_list, name="restodab.views.postre_list"),
        url(r'^guarnicion/$', views.guarnicion_list, name="restodab.views.guarnicion_list"),
        url(r'^lunch/$', views.lunch_list, name="restodab.views.lunch_list"),
        url(r'^breakfast/$', views.breakfast_list, name="restodab.views.breakfast_list"),
        url(r'^producto/(?P<pk>[0-9]+)/$', views.producto),
]
