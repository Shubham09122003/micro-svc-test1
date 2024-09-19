from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello", content_type="application/json")