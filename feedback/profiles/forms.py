from django import forms

class ProfielForm(forms.Form):
  user_image = forms.FileField(required=False)