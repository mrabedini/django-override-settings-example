from django.shortcuts import render
from django.http import HttpResponse

from .config import APP_SAMPLE_CONFIG
# Create your views here.

def sample_view(request):
    return HttpResponse(APP_SAMPLE_CONFIG)
    

