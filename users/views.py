from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello my dev", content_type="application/json")