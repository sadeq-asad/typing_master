from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def render_mainpage(request):
    return HttpResponse("MAIN PAGE")