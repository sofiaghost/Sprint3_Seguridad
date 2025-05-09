from ..models import Evento

def is_valid_input(user_input):
    
    suspicious_patterns = [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"(\%3D)|(\=)",  
        r"(\%2F)|(\//)",  
        r"(\%2D)|(\-)", 
        r"(\%22)|(\")",  
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, user_input):
            return False  # Si encuentra un patrón sospechoso, es inválido
    return True  # Si no hay patrones sospechosos, es válido

def get_eventos():
    try:
        # Obtener todos los eventos
        queryset = Evento.objects.all()
        return queryset
    except Exception as e:
        raise Exception(f"Error al obtener los eventos: {str(e)}")
    
    
def create_evento(form):
    evento = form.save()
    evento.save()
    return ()
