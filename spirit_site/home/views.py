# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def spirit(request):
    my_dict={'insert':"check templates"}
    return render(request,'home/home.html',context = my_dict)

def organizingteam(request):
    return render(request,'home/organizingteam.html')

def gallery(request):
    return render(request,'home/gallary.html')

def athletics(request):
    return render(request,'home/athletics.html')

def badminton(request):
    return render(request,'home/badminton.html')

def basketball(request):
    return render(request,'home/basketball.html')

def cricket(request):
    return render(request,'home/cricket.html')

def lawntennis(request):
    return render(request,'home/lawntennis.html')

def volleball(request):
    return render(request,'home/volleyball.html')

def football(request):
    return render(request,'home/football.html')

def chess(request):
    return render(request,'home/chess.html')

def hockey(request):
    return render(request,'home/hockey.html')

def tabletennis(request):
    return render(request,'home/tabletennis.html')

def volleyball(request):
    return render(request,'home/volleyball.html')
