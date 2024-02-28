from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
    return render(request, 'portfolio_app/index.html')

def login():
    return HttpResponse('login page')

def logout():
    return HttpResponse('logout page')