from django.db import models

# aca vamos a crear nuestras tablas a la base de datos
#modelo para el sexo
class Sexo (models.Model):
    id_sexo = models.IntegerField(primary_key=True),
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.sexo
#modelo para la persona
class Persona(models.Model):
    rut = models.CharField(primary_key=True,max_length=10 )
    nombre = models.CharField(max_length=40 )
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE,null=True)
    fechaNac = models.CharField(max_length=8 , verbose_name="fecha nacimiento")
    telefono = models.CharField(max_length=9)
    antecedentes = models.TextField(max_length=200,null=True)
    fechaIng = models.CharField(max_length=8,null=True , verbose_name="fecha Ingreso")    

def __str__(self):
    return self.rut

class Evolucion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.CharField(max_length=8)
    rutPaciente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    evolucion = models.TextField(max_length=200)

def __str__(self):
    return self.id 

class Aportadores(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=40 )
    correo = models.CharField(max_length=50 )
    contraseña = models.CharField(max_length=10)

def __str__(self):
    return self.id

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

def __str__(self):
    return self.id     

class MandatoAportador(models.Model):
    id  = models.AutoField(primary_key=True)
    monto = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nro_tarjeta = models.CharField(max_length=30)
    dia_pago = models.CharField(max_length=2)
    fecha_transaccion = models.CharField(max_length=10)

class pagosAportador(models.Model):
    id_pago = models.AutoField(primary_key=True)                
    id_aportador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    codigo_transaccion = models.CharField(max_length=30)
    fecha_pago = models.CharField(max_length=10)
    monto = models.IntegerField()

class Gastos (models.Model):
    id_gasto = models.AutoField(primary_key=True)
    fecha_gasto = models.DateTimeField(auto_now_add=True)
    monto = models.IntegerField()
    detalle =  models.CharField(max_length=300)

class Medicamentos (models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=40)
    formato = models.CharField(max_length=30)
    codigo = models.CharField(max_length=40)
    valor = models.IntegerField()
    cantidad = models.IntegerField(null=True)
    precio_Total = models.IntegerField(null=True)

class Bodega  (models.Model):
    id_bodega = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=40)
    valor = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()