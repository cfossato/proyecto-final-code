from django import forms


class reservaFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    fechaDeEntrada= forms.DateField()
    pagado= forms.BooleanField()
    imagenreserva = forms.ImageField(required=True) 


