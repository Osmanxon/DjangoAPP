from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def HomePage(requests):
    # return HttpResponse("Bu bosh sahifa")
    return render(requests, "home.html")