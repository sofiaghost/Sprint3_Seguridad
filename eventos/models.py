from django.db import models
from historias.models import Historia


class Evento(models.Model):
    fecha=models.DateField()
    historiaPaciente=models.ForeignKey(Historia, on_delete=models.CASCADE, default=None)
    especialidad=models.CharField(max_length=100, default="Consulta General")
    comentarios=models.TextField(default=None)
    
    def __str__(self):
        return '{}'.format(self.historiaPaciente.id+' - '+self.fecha.strftime('%Y-%m-%d')+' - '+self.especialidad[0:4])