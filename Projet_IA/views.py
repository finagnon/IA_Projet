from django.shortcuts import render

from django.http import HttpResponse


def good_view(request):
    return  render(request, 'good.html')

def bad_view(request):
    return  render(request, 'bad.html')

def verify_view(request):
    return  render(request, 'verify.html')

def contact_view(request):
    return  render(request, 'contact.html')

def home_view(request):
    return  render(request, 'index.html')

