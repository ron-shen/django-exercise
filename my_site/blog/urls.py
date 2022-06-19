from django.urls import URLPattern
from django.urls import path
from . import views


urlpatterns = [
  path("", views.StartingPageView.as_view(), name="home_page"),  #/home page
  path("posts", views.AllPostView.as_view(), name="posts-page"),   
  path("posts/<slug:slug>", views.SinglePostView.as_view(), name="indiviudal-post")
]