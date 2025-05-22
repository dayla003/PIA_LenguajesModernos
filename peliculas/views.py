from django.http import HttpResponse
from django.template import loader
from .models import Pelicula
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PeliculaForm


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def peliculas(request):
    query = request.GET.get('q')
    if query:
        peliculas = Pelicula.objects.filter(titulo__icontains=query)
    else:
        peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {
        'peliculas': peliculas,
        'query': query
    })

def agregar(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/agregar.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('peliculas')

    return render(request, 'peliculas/editar.html', {'formulario': formulario})


def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas')
