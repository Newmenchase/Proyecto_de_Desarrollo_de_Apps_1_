from django.shortcuts import render, redirect
from .models import Rutina
from .forms import RutinaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_rutinas(request):
    rutinas = Rutina.objects.filter(usuario=request.user)
    return render(request, 'entrenamientos/lista_rutinas.html', {'rutinas': rutinas}
    )

@login_required
def crear_rutina(request):
    if request.method == 'POST':
        form = RutinaForm(request.POST, request.FILES)

        if form.is_valid():
            rutina = form.save(commit=False)
            rutina.usuario = request.user
            rutina.save()
            return redirect('lista_rutinas')

    else:
        form = RutinaForm()

    return render(request, 'entrenamientos/crear_rutina.html', {
        'form': form
    })
def detalle_rutina(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)

    return render(request, 'entrenamientos/detalle_rutina.html', {
        'rutina': rutina
    })
@login_required
def editar_rutina(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)

    if request.method == 'POST':
        form = RutinaForm(request.POST, request.FILES, instance=rutina)

        if form.is_valid():
            form.save()
            return redirect('lista_rutinas')

    else:
        form = RutinaForm(instance=rutina)

    return render(request, 'entrenamientos/editar_rutina.html', {
        'form': form
    })
@login_required
def eliminar_rutina(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)

    if request.method == 'POST':
        rutina.delete()
        return redirect('lista_rutinas')

    return render(request, 'entrenamientos/eliminar_rutina.html', {
        'rutina': rutina
    })