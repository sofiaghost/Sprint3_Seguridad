from django.shortcuts import render
from .forms import EventoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_eventos import create_evento, get_eventos
from django.contrib.auth.decorators import login_required


@login_required
def evento_list(request):
    try:
        imgs = get_eventos()
        context = {
            'evento_list': imgs
        }
        return render(request, 'Evento/eventos.html', context)
    except Exception as e:
        # Si ocurre un error al obtener los eventos, se muestra un mensaje
        messages.error(request, f"Error al obtener los eventos: {str(e)}")
        return HttpResponse(f"Error al obtener los eventos: {str(e)}", status=500)



@login_required
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            try:
                create_evento(form)
                messages.add_message(request, messages.SUCCESS, 'Evento creado')
                return HttpResponseRedirect(reverse('eventoCreate'))
            except Exception as e:
                # Si ocurre un error al crear el evento, se muestra un mensaje
                messages.error(request, f"Error al crear el evento: {str(e)}")
                return HttpResponse(f"Error al crear el evento: {str(e)}", status=500)
        else:
            print(form.errors)
    else:
        form = EventoForm()

    context = {
        'form': form,
    }

    return render(request, 'Evento/eventoCreate.html', context)