# SARA LOGIN YAHAN LIKHA JATA HAI. THIS CAN DIRECTLY TALK TO MODELS OR VIA A URL.

# this ensure that now user is ready to take respond and request from client
from django.http import HttpResponse
from django.shortcuts import render

# making a function for our response
def home(request):
    # return HttpResponse("hey from PROJECT:2 :)")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("hey from about page of PROJECT:2 :)")

def contact(request):
    return HttpResponse("hey from contact page of PROJECT:2 :)")
