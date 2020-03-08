from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def do_acu(request):
    return HttpResponse('HELLO')
def do_ACU(requesy,year,month):
    return HttpResponse('this is {0}year {1}month'.format(year,month))
def do_app(request):
    return HttpResponse("这是个子路由")