from django.shortcuts import render, get_object_or_404,redirect
from gestorapp.models import Plantel, Docente, Alumno
from gestorapp.forms import PlantelForm, DocenteForm, AlumnoForm

# Create your views here.
def detalleAlumno(request,id):
    alumno = get_object_or_404(Alumno,pk=id)
    return render(request,'detalleAlu.html',{'alumno':alumno})

def nuevoAlumno(request):
    if request.method == "POST":
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('index')
    else:
        formaAlumno=AlumnoForm()
        return render(request,'agregarAlu.html',{'formaAlumno':formaAlumno})

def editarAlumno(request, id):
    alumno = get_object_or_404(Alumno,pk=id)
    if request.method == "POST":
        formaAlumno = AlumnoForm(request.POST, instance=alumno)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('index')
    else:
        formaAlumno = AlumnoForm(instance=alumno)
        return render(request,'editarAlu.html',{'formaAlumno':formaAlumno})

def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumno,pk=id)
    if alumno:
        alumno.delete()
    return redirect('index')

def detalleDocente(request, id):
    docente = get_object_or_404(Docente,pk=id)
    return render(request,'detalleDoc.html',{'docente':docente})

def nuevoDocente(request):
    if request.method == "POST":
        formaDocente = DocenteForm(request.POST)
        if formaDocente.is_valid():
            formaDocente.save()
            return redirect('index')
    else:
        formaDocente=DocenteForm()
        return render(request,'agregarDoc.html',{'formaDocente':formaDocente})

def editarDocente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    if request.method == "POST":
        formaDocente = DocenteForm(request.POST, instance=docente)
        if formaDocente.is_valid():
            formaDocente.save()
            return redirect('index')
    else:
        formaDocente = DocenteForm(instance=docente)
        return render(request,'editarDoc.html',{'formaDocente':formaDocente})

def eliminarDocente(request, id):
    docente = get_object_or_404(Docente,pk=id)
    if docente:
        docente.delete()
    return redirect('index')

def detallePlantel(request,id):
    plantel = get_object_or_404(Plantel,pk=id)
    return render(request,'detallePlan.html',{'plantel':plantel})

def nuevoPlantel(request):
    if request.method == "POST":
        formaPlantel = PlantelForm(request.POST)
        if formaPlantel.is_valid():
            formaPlantel.save()
            return redirect('index')
    else:
        formaPlantel=PlantelForm()
        return render(request,'agregarPlan.html',{'formaPlantel':formaPlantel})

def editarPlantel(request, id):
    plantel = get_object_or_404(Plantel, pk=id)
    if request.method == "POST":
        formaPlantel = PlantelForm(request.POST, instance=plantel)
        if formaPlantel.is_valid():
            formaPlantel.save()
            return redirect('index')
    else:
        formaPlantel = PlantelForm(instance=plantel)
        return render(request,'editarPlan.html',{'formaPlantel':formaPlantel})

def eliminarPlantel(request, id):
    plantel = get_object_or_404(Plantel,pk=id)
    if plantel:
        plantel.delete()
    return redirect('index')