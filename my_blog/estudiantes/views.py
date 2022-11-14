from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def estudiantes (request) :
    return HttpResponse ('vista estudiantes')