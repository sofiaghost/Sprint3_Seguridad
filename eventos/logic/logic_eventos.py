from ..models import Evento


def get_eventos():
    queryset = Evento.objects.all()
    return (queryset)

def create_evento(form):
    evento = form.save()
    evento.save()
    return ()