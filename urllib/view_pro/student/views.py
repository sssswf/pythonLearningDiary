from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def check_name(request):
    return HttpResponse("这是一个子路由")