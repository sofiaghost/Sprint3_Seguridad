from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'paciente',
            'cc',
            #'fecha',
        ]
        labels = {
            'paciente' : 'Paciente',
            'cc' : 'CC',
            #'fecha' : 'Fecha',
        }