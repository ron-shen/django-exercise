import re
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpRequest
from .forms import ProfielForm
# Create your views here.

def store_file(file):
    with open("temp/qwe.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
            

class CreateProfileView(View):
    def get(self, request):
        form = ProfielForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfielForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            store_file(request.FILES["user_image"])
            return HttpResponseRedirect("profiles")
        return render(request, "profiles/create_profile.html", {"form": submitted_form})
