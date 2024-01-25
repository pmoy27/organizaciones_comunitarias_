from django.db import models

class Organizacion(models.Model):
    rut_directiva = models.CharField(max_length=15, null=True, blank=True)
    tipo_de_organizacion = models.CharField(max_length=100, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    rol_municipalidad = models.IntegerField(null=False, blank=False)
    fecha_concesion_p_j = models.DateField()
    numero_inscripcion_rc = models.IntegerField(null=False, blank=False)   
    sede_lugar_funcionamiento = models.CharField(max_length=100, null=False, blank=False)
    directiva = models.CharField(max_length=100, null=False, blank=False)  
    vigencia_directiva = models.CharField(max_length=100, null=False, blank=False)
    estatuto = models.DateField()
    fecha_termino_directiva = models.DateField(null=True, blank=True)

class Usuario(models.Model):
    correo = models.CharField(max_length=100, null=False, blank=False)
    contrasena = models.CharField(max_length=50, null=False, blank=False)
