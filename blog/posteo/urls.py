from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^listar/$',"posteo.views.listar_post"),
    url(r'^detalle/$',"posteo.views.detalle_post"),
    url(r'^crear/$',"posteo.views.crear_post"),
    url(r'^actualizar/$',"posteo.views.actualizar_post"),
    url(r'^borrar/$',"posteo.views.borrar_post"),

]
