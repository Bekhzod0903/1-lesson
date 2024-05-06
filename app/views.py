from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_info(request):
    return HttpResponse('Hello World')


def get_name(request):
    return HttpResponse('Begzod')

def get_surname(request):
    return HttpResponse('Shomurodov')

def get_age(request):
    return HttpResponse('20')

def get_city(request):
    return HttpResponse('Tashkent')

def get_country(request):
    return HttpResponse('Uzbekistan')

def get_email(request):
    return HttpResponse('gfewjwg@gmail.com')

def get_phone(request):
    return HttpResponse('+998999999999')

def get_university(request):
    return HttpResponse('Tashkent University')

def get_faculty(request):
    return HttpResponse('Faculty of Computer Science')
def get_gender(request):
    return HttpResponse('Male')