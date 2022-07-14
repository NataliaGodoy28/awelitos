from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Evolucion, MandatoAportador, Persona, Usuario


#creamos nuestra clase para formulario
class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = ['rut','nombre','sexo','fechaNac','telefono','antecedentes','fechaIng']

class modificarPersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = ['rut','nombre','sexo','fechaNac','telefono','antecedentes','fechaIng']

class evolucionesForm (ModelForm):
    class Meta:
        model = Evolucion
        fields =['fecha_creacion','rutPaciente','evolucion']

class usuarioForm (ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','correo','contraseña']

class loginForm (ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['correo','contraseña']

class mandatoForm (ModelForm):
    class Meta:
        model = MandatoAportador
        fields = ['monto','id_usuario','nro_tarjeta','dia_pago','fecha_transaccion']