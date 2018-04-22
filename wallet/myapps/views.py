from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def site(request):
    return render(request, 'myapps/1.htm', {})
# Create your views here.
