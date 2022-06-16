from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class RviewView(View):
  def get(self, request):
    form = ReviewForm()  
    return render(request, "reviews/review.html", {"form": form})
  
  def post(self, request):
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/thank-you")

# def review(request):
#   if request.method == 'POST':
#     existing_data = Review.objects.get(pk=1)
#     form = ReviewForm(request.POST, instance=existing_data)
#     if form.is_valid():
#       review.save()
#       return HttpResponseRedirect("/thank-you")
  
  

def thank_you(request):
  return render(request, "reviews/thank_you.html") 