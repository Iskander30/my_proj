from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('Успешно')

def index(request):
    return render(request, 'index.html')

def top-sellers(request):
    return render(request, 'top-sellers.html')
