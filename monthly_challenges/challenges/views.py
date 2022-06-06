from turtle import forward
from wsgiref.util import shift_path_info
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
  "january": 1,
  "february": 2,
  "march": 3,
  "april": 4,
  "may": 5,
  "june": None
}

# Create your views here.
def monthly_challenge(request, month):
  if month in monthly_challenges:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month": month    
    })
    
  raise Http404()


def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  forward_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[forward_month])
  return HttpResponseRedirect(redirect_path)


def index(request):
  months = list(monthly_challenges.keys())
  return render(request, "challenges/index.html", {
    "months": months
  })
  
  