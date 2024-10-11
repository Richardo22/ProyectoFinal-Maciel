from django import forms


class EmpanadaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    ingredientes = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class HamburguesaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    ingredientes = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class PizzaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    ingredientes = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    