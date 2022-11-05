from tkinter.tix import Form
from unittest.util import _MAX_LENGTH
from django import forms


class FormularioPlatos(forms.Form):
    PLATOS = (
        (1, 'Entradas'),
        (2, "Plato Fuerte"),
        (3, "Postre")
    )
    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    descripcion = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'resize:none'
        })
    )
    fotografia = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    precio = forms.CharField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    tipo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }), choices=PLATOS
    )
