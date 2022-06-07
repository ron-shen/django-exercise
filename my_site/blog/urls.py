from django.urls import URLPattern
from django.urls import path
from . import views


urlpatterns = [
  path("", views.homepage, name="home_page"),  #/home page
  path("posts", views.posts, name="posts-page"),   
  path("posts/<slug:slug>", views.indiviudal_post, name="indiviudal-post")
]