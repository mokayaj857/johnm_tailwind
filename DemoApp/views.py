from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage (Response):
    content="<html><body><h1><\h1>This is h1 for homepage<\body><\html>"
    return HttpResponse(content)