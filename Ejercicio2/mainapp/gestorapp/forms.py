from django.forms import ModelForm
from gestorapp.models import Docente, Alumno, Plantel, Carrera, Domicilio

class PlantelForm(ModelForm):
    class Meta:
        model = Plantel
        fields = '__all__'

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'