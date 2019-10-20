from django.shortcuts import render
from .forms import SaludarForm

def saludar(request):
    form = SaludarForm()
    if request.method == 'POST':
        form = SaludarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            return render(request, 'nombre.html', {'nombre': nombre})        
    return render(request, 'form.html', {'form': form})
