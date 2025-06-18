# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Athletes
from .forms import AthletesForm

def lista_athletes(request):
    athletes = Athletes.objects.all()
    return render(request, 'core/lista_athletes.html', {'athletes': athletes})

def crear_athlete(request):
    if request.method == 'POST':
        form = AthletesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_athletes')
    else:
        form = AthletesForm()
    return render(request, 'core/form_athlete.html', {'form': form})

def editar_athlete(request, pk):
    athlete = get_object_or_404(Athletes, pk=pk)
    if request.method == 'POST':
        form = AthletesForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect('lista_athletes')
    else:
        form = AthletesForm(instance=athlete)
    return render(request, 'core/form_athlete.html', {'form': form})

def borrar_athlete(request, pk):
    athlete = get_object_or_404(Athletes, pk=pk)
    if request.method == 'POST':
        athlete.delete()
        return redirect('lista_athletes')
    return render(request, 'core/confirm_delete_athlete.html', {'object': athlete})
