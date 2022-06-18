from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView, DetailView
from .models import Review

# Create your views here.

# class RviewView(FormView):
#   form_class = ReviewForm
#   template_name = "reviews/review.html"
#   success_url = "thank-you"
#   def form_valid(self, form):
#     form.save()
#     return super().form_valid(form)
  
class RviewView(CreateView):
  model = Review
  form_class = ReviewForm
  template_name = "reviews/review.html"
  success_url = "thank-you"


class ThankYouView(TemplateView):
  template_name = "reviews/thank_you.html"
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['message'] = "hi"
      return context
  
class ReviewListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = "reviews"
  
  # def get_queryset(self):
  #     base_query = super().get_queryset()
  #     data = base_query.filter(rating__gt=4)
  #     return data
    
class SingleReviewView(DetailView):
  template_name = "reviews/single_review.html"
  model = Review
  
  def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      loaded_review = self.object
      request = self.request
      favorite_id = request.session.get("favorite_review")
      context["is_favorite"] = favorite_id == str(loaded_review.id)
      return context
  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     review_id = kwargs["id"]
  #     selected_review = Review.objects.get(pk=review_id)
  #     context["review"] = selected_review
  #     return context  
  
  
class AddFavoriteView(View):
  def post(self, request):
    review_id = request.POST['review_id']
    print(review_id)
    # #fav_review = Review.objects.get(pk=review_id)
    request.session['favorite_review'] = review_id
    return HttpResponseRedirect("/reviews/" + review_id)
    #return HttpResponseRedirect("thank-you")
    