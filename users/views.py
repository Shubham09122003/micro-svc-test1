from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    users =[{"user_id":"shubh","age":20},{"user_id":"Amit","age":22}]
    return HttpResponse(users, content_type="application/json")