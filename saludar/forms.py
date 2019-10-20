from django import forms

class SaludarForm(forms.Form):
    nombre = forms.CharField()

