from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def render_mainpage(request):
    return render(request, "TypingMasterApp/main_page.html", {})