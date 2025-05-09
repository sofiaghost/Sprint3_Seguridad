from ..models import Historia

def get_historias():
    queryset = Historia.objects.all()
    return (queryset)


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


def get_historia_by_id(id):
    try:
        if not is_valid_input(id):  # Validar el parámetro de entrada
            raise ValueError("Entrada inválida detectada.")
        
        historia = Historia.objects.get(id=id)
        return historia
    except Historia.DoesNotExist:
        return None
    except ValueError as e:
        raise ValueError(f"Error: {str(e)}")
    except Exception as e:
        raise Exception(f"Error al obtener la historia: {str(e)}")
    
    
def create_historia(form):
    measurement = form.save()
    measurement.save()
    return ()
