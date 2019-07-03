from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'booktest/index.html',{'username':'zzy'})
def detail(request,id):
    book = BookInfo.objects.get(pk = id)
    return render(request,'booktest/detail.html',{'book':book})
def list(request):
    booklist = BookInfo.objects.all()
    return HttpResponse(request,'booktest/list.html',{'booklist':booklist})