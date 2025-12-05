from django import forms

class GuessNumberForm(forms.Form):
    number = forms.IntegerField(label="Enter a number")