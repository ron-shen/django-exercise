from django import forms

class ProfielForm(forms.Form):
  user_image = forms.ImageField(required=False)