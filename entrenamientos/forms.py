from django import forms
from .models import Rutina


class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        exclude = ['usuario']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nombre de la rutina'
            }),

            'tipo': forms.Select(attrs={
                'class': 'input'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'input',
                'rows': 4,
                'placeholder': 'Describe la rutina'
            }),
        }