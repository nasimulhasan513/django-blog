from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('This is an about page')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('This is an about page')
    return render(request, 'about.html')
