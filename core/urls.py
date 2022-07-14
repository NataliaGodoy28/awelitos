from unittest.mock import patch
from django.urls import path
from .views import *

#aca estan todas las url para que sean visibles por el view
urlpatterns = [
    path('', home, name="home"),
    path('crud', crud, name="crud"),
    path('agregarForm', agregarForm, name="agregarForm"),
    path('fundacion', fundacion, name="fundacion"),
    path('fichaClinica/<id>', fichaClinica , name="fichaClinica"),
    path('evoluciones/<id>', evoluciones, name="evoluciones"),
    path('evolucionesAntiguas/<id>', evolucionesAntiguas, name="evolucionesAntiguas"),
    path('historial', historial , name="historial"),
    path('mDiaria', mDiaria , name="mDiaria"),
    path('modificarPersona/<id>', modificarPersona , name="modificarPersona"),
    path('eliminarPersona/<id>', eliminarPersona , name="eliminarPersona"),
    path('perfilAportador', perfilAportador , name="perfilAportador"),
    path('reportes', reportes , name="reportes"),
    path('mandato', mandato , name="mandato"),  
    path('reporteAportador/', reporteAportador , name="reporteAportador"),  
    path('aportadores', aportadores , name="aportadores"),  
    path('farmacia', farmacia , name="farmacia"),  
    path('recaudacion', recaudacion , name="recaudacion"),
    path('bodega', bodega , name="bodega"),
    path('login', login , name="login"),

]
