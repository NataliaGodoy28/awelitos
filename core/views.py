from django.shortcuts import redirect, render
from core.forms import PersonaForm
from .models import Bodega, Gastos, Persona, Evolucion, pagosAportador, Usuario, Medicamentos
from .forms import PersonaForm, evolucionesForm, mandatoForm, usuarioForm, loginForm
from django.db.models import Sum
import logging
logger = logging.getLogger(__name__)

# aca creamos nuestro diccionario de url


def fundacion(request):
    return render(request, 'core/principal.html')


def bodega(request):
    email = request.session['username']
    print(request.session['username'])
    usuario = Usuario.objects.get(correo=email)
    bodega = Bodega.objects.all()
    datos = {'bodega': bodega , 'usuario':usuario}
    return render(request, 'core/bodega.html',datos)


def reportes(request):
   # aca podemos hacer un joihn en mas tablas de la base de datos
    nombre = Usuario.objects.all().select_related('id').values('pagosaportador', 'nombre', 'apellido', 'pagosaportador__id_aportador',
                                                               'pagosaportador__fecha_pago', 'pagosaportador__monto', 'pagosaportador__codigo_transaccion')
    ingresos = pagosAportador.objects.all()
    datos = {'ingresos': ingresos, 'nombre': nombre}

    return render(request, 'core/reportes.html', datos)


def recaudacion(request):
    pagos = pagosAportador.objects.all()
    gastos = Gastos.objects.all()
    
    nombre = Usuario.objects.all().select_related('id').values('pagosaportador', 'nombre', 'apellido',
                                                                              'pagosaportador__id_aportador', 'pagosaportador__fecha_pago', 'pagosaportador__monto', 'pagosaportador__codigo_transaccion')
    

    suma_gasto = Gastos.objects.all().aggregate(sum=Sum('monto'))['sum']
    suma_ingreso = pagosAportador.objects.all().aggregate(sum=Sum('monto'))[
        'sum']
    total = suma_ingreso-suma_gasto
    datos = {'pagos': pagos, 'gastos': gastos, 'suma_gasto': suma_gasto,
             'suma_ingreso': suma_ingreso, 'total': total , 'nombre': nombre}

    return render(request, 'core/recaudacion.html', datos)


def farmacia(request):

    medicamentos = Medicamentos.objects.all()
    datos = {'farmacia': medicamentos}

    return render(request, 'core/farmacia.html', datos)


def aportadores(request):

    usuarios = Usuario.objects.all()

    datos = {'usuarios': usuarios}

    return render(request, 'core/aportadores.html', datos)


def mandato(request):
    email = request.session['username']
    print(request.session['username'])
    usuario = Usuario.objects.get(correo=email)
    datos = {'form': mandatoForm , 'usuario':usuario }
    # verificamos peticion post
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = mandatoForm(request.POST)
        # VALIDAMOS EL FORMULARIO
        if formulario.is_valid:
            # ahora guardamos en la base de datos
            formulario.save()
            # y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"

            return redirect(to="perfilAportador")
    return render(request, 'core/mandato.html', datos)


def evoluciones(request):
    return render(request, 'core/evoluciones.html')


def perfilAportador(request):
    return render(request, 'core/perfilAportador.html')


def evolucionesAntiguas(request):
    return render(request, 'core/evolucionesAntiguas.html')


def historial(request):
    return render(request, 'core/historial.html')


def mDiaria(request):
    return render(request, 'core/mDiaria.html')

# pasaremos por parametros los datos


def crud(request):

    personas = Persona.objects.all()
    lista = ["Java", "Python", ".net", "PHP"]
    contexto = {'lenguajes': lista, 'personas': personas}

    return render(request, 'core/crudPacientes.html', contexto)


def agregarForm1(request):

    personas = Persona.objects.all()
    lista = ["Java", "Python", ".net", "PHP"]
    contexto = {'nombre': 'Juan Perez',
                'lenguajes': lista, 'personas': personas}

    return render(request, 'core/agregarForm.html', contexto)


# para agregar a la base de datos los pacientes
def agregarForm(request):

    datos = {'form': PersonaForm(), 'nombre': 'juan perez'
             }
    # verificamos peticion post
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = PersonaForm(request.POST)
        # VALIDAMOS EL FORMULARIO
        if formulario.is_valid:
            # ahora guardamos en la base de datos
            formulario.save()
            # y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/agregarForm.html', datos)


def modificarPersona(request, id):
    persona = Persona.objects.get(rut=id)
    datos = {"form": PersonaForm(instance=persona)}
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Persona Modificada con exito!."
            datos["form"] = form

            return redirect(to="crud")

    return render(request, 'core/modificarPersona.html', datos)


def eliminarPersona(request, id):
    persona = Persona.objects.get(rut=id)
    # el id es el identificador
    # eliminamos la persona con el id buscado
    persona.delete()
    # nos dirigimos a la pagina dnde esta el listado
    return redirect(to="crud")


def fichaClinica(request, id):
    persona = Persona.objects.get(rut=id)
    evolucion = Evolucion.objects.filter(rutPaciente=id).last()
    datos = {'persona': persona, 'evolucion': evolucion}

    return render(request, 'core/fichaClinica.html', datos)


def evoluciones(request, id):
    persona = Persona.objects.get(rut=id)
    evolucion = Evolucion.objects.filter(rutPaciente=id).first()
    datos = {'persona': persona, 'form': evolucionesForm(),
             'evolucion': evolucion}
    # verificamos peticion post
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = evolucionesForm(request.POST)
        # VALIDAMOS EL FORMULARIO
        if formulario.is_valid:
            # ahora guardamos en la base de datos
            formulario.save()
            # y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/evoluciones.html', datos)


def evolucionesAntiguas(request, id):
    persona = Persona.objects.get(rut=id)
    evolucion = Evolucion.objects.filter(rutPaciente=id).all()
    datos = {'persona': persona, 'evolucion': evolucion}
    return render(request, 'core/evolucionesAntiguas.html', datos)


def reporteAportador(request):
    email = request.session['username']
    print(request.session['username'])
    
    suma_aporte = Usuario.objects.filter(correo=email).select_related('id').values('pagosaportador',
                                                                              'pagosaportador__id_aportador', 'pagosaportador__monto').aggregate(sum=Sum('pagosaportador__monto'))['sum']

    usuario = Usuario.objects.get(correo=email)
    nombre = Usuario.objects.filter(correo=email).select_related('id').values('pagosaportador', 'nombre', 'apellido',
                                                                              'pagosaportador__id_aportador', 'pagosaportador__fecha_pago', 'pagosaportador__monto', 'pagosaportador__codigo_transaccion')
    datos = {'usuario': usuario, 'nombre': nombre, 'suma_aporte': suma_aporte}
    return render(request, 'core/reporteAportador.html', datos)


def home(request):

    datos = {'form': usuarioForm()
             }
    logging.info('So should this')
    logging.info(datos)

    # verificamos peticion post
    if request.method == 'POST':
        logger.info('page_processor logging test')
        # con request recuperamos los datos del formulario
        formulario = usuarioForm(request.POST)
        formularioLogin = loginForm(request.POST)
        # VALIDAMOS EL FORMULARIO
        if formulario.is_valid:
            # ahora guardamos en la base de datos
            formulario.save()
            # y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"
            return redirect(to="login   ")

    return render(request, 'core/home.html', datos)


def login(request):
    datos = {'form': loginForm()
             }
    if request.method == 'POST':
        formulario = loginForm(request.POST)
        print(request.POST['correo'])
        email = request.POST['correo']
        usuario = Usuario.objects.filter(correo=email)
        emp = request.session['username'] = email
        if not usuario:
            print('esta vacio')
            return redirect(to="login")

        if email == 'admin@gmail.com':
            return redirect(to="crud")

        if usuario:
            print('esta gordito')

            return redirect(to="reporteAportador")

    return render(request, 'core/login.html', datos)
