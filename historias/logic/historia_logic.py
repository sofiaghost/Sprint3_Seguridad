from ..models import Historia

def get_historias():
    queryset = Historia.objects.all()
    return (queryset)

def get_historia_by_id(id):
    # Usamos raw() para ejecutar la consulta SQL
    historia = Historia.objects.raw("SELECT * FROM historias_historia WHERE id = %s", [id])
    
    # Si hay resultados, retornamos el primero
    if historia:
        return historia[0]  # El primer resultado
    else:
        return None  # No se encontró la historia



def create_historia(form):
    measurement = form.save()
    measurement.save()
    return ()