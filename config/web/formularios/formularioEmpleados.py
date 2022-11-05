from django import forms


class FormularioEmpleados(forms.Form):
    cargo = (
        (1, 'Chef'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Ayudante')
    )
    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    apellidos = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    foto = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    cargo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }), choices=cargo
    )
    salario = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    contacto = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
