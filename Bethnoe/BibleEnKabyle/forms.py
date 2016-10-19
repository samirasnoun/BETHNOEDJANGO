from django import forms

class Recherche(forms.Form):
    text_recherche = forms.CharField(label='Texte de recherche ', max_length=100, required=False)