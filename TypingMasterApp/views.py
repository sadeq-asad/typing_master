from django.shortcuts import render
from .models import TypingMaster
from django.http import HttpResponse

# Create your views here.

def render_mainpage(request):
    return render(request, "TypingMasterApp/main_page.html", {})

def get_input(request):
    all_objects = TypingMaster.objects.all()
    return render(request, "TypingMasterApp/get_input.html", {'all_objects':all_objects})

def measure_speed(request):
    typist = request.GET["typist_name"]
    words_typed = request.GET["text"]
    if words_typed:
        words_typed = words_typed.split(" ")
        return HttpResponse ("%s typed %d words" % (typist, len(words_typed)))
    else:
        return HttpResponse("You haven't typed any word!")    