from django.shortcuts import render
from .forms import EventoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_eventos import create_evento, get_eventos
from django.contrib.auth.decorators import login_required


@login_required
def evento_list(request):
    imgs = get_eventos()
    context = {
        'evento_list': imgs
    }
    return render(request, 'Evento/eventos.html', context)


def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            create_evento(form)
            messages.add_message(request, messages.SUCCESS, 'Evento creado')
            return HttpResponseRedirect(reverse('eventoCreate'))
        else:
            print(form.errors)
    else:
        form = EventoForm()

    context = {
        'form': form,
    }

    return render(request, 'Evento/eventoCreate.html', context)