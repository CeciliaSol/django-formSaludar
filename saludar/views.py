from django.shortcuts import render, redirect, get_object_or_404
from .forms import IndexForm
from .models import Tarea


def index(request):
	form = IndexForm()
	if request.method == 'POST':
		form = IndexForm(request.POST)

		if form.is_valid():
			tarea = form.cleaned_data['tarea']
			Tarea.objects.create(tarea=tarea)

			return redirect('/index')
	return render(request, 'index.html', {'form': form})


def listado(request):
	listado = Tarea.objects.all()
	return render(request, 'listado.html', {'listado':listado})

def terminado(request, id):
	tarea = get_object_or_404(Tarea, pk=id)
	tarea.estado = True
	tarea.save()
	return redirect('/index')

	