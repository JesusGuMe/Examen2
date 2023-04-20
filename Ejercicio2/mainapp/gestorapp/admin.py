from django.contrib import admin
from gestorapp.models import Carrera, Domicilio, Alumno, Docente, Plantel
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Domicilio)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Plantel)