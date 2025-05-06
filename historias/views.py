from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .forms import HistoriaForm
from .logic.historia_logic import get_historias, get_historia_by_id, create_historia
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole  # Descomentar cuando se cree el archivo



@login_required
def historia_list(request):
    role = getRole(request)
    if role in ["Médico Especializado", "Enfermero", "Enfermera"]:
        try:
            historias = get_historias()
            context = {
                'historia_list': historias
            }
            return render(request, 'Historia/historias.html', context)
        except Exception as e:
            return HttpResponse(f"Error al obtener las historias clínicas: {str(e)}", status=500)
    return HttpResponse("Usuario no autorizado", status=401)

@login_required
def single_historia(request, historia_id):
    role = getRole(request)
    if role in ["Médico Especializado", "Enfermero", "Enfermera"]:
        try:
            historia = get_historia_by_id(historia_id)
            if not historia:
                raise Http404("Historia clínica no encontrada")
            context = {'historia': historia}
            return render(request, 'Historia/historia.html', context)
        except Exception as e:
            return HttpResponse(f"Error al acceder a la historia clínica: {str(e)}", status=500)
    return HttpResponse("Usuario no autorizado", status=401)

@login_required
def historia_create(request):
    role = getRole(request)
    if role in ["Médico Especializado", "Enfermero", "Enfermera"]:
        if request.method == 'POST':
            form = HistoriaForm(request.POST)
            if form.is_valid():
            
                    # Pasamos el formulario directamente sin sanitización manual
                    create_historia(form)
                    messages.add_message(request, messages.SUCCESS, 'Historia creada')
                    return HttpResponseRedirect(reverse('historiaCreate'))
            else:
                 print(form.errors)

        else:
            form = HistoriaForm()

        context = {'form': form}
        return render(request, 'Historia/historiaCreate.html', context)
    
    return HttpResponse("Usuario no autorizado", status=401)


