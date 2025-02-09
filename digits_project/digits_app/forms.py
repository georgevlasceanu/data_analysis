from django import forms

class ImagePredictForm(forms.Form):
    image = forms.ImageField()