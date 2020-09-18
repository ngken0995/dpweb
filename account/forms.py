from django import forms

class HappinessForm(forms.Form):
    scale = forms.IntegerField(min_value= 1,max_value=10)
