from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your Name", error_messages={"required": "Your name cannot be empty"})
#   review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['user_name', 'review_text', 'rating']
    labels = {'user_name': 'Your name', 'review_text': "Your Feedback", 'rating': "Your rating"}
    error_messages = {
      'user_name': {
        "required": "Your name cannot be empty",
        "max_length": "too long!"
      }
    }
  