from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
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
    return render(request,'booktest/list.html',{'booklist':booklist})
def addhero(request,id):
    book = BookInfo.objects.get(pk = id)
    if request.method == 'GET':
        return render(request,'booktest/addhero.html',{'book':book})
    elif request.method == 'POST':
        name = request.POST.get('name')
        skill= request.POST.get('skill')
        hero = HeroInfo()
        hero.name = name
        hero.skill = skill
        hero.book = book
        hero.save()
        return redirect(reverse('booktest:detail',args=(id,)))
def addbook(request):
    # booklist = BookInfo()
    if request.method == 'GET':
        # print("------------yemian-----------------")
        return render(request,'booktest/addbook.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        time = request.POST.get('time')
        book = BookInfo()
        book.pub_date=time
        book.title = title
        book.save()
        # print("---------888--------------------")
        return redirect(reverse('booktest:list',))

def deletebook(request,id):
    book = BookInfo.objects.get( pk = id)
    book.delete()
    return redirect(reverse('booktest:list'))



def deletehero(request,id):
    hero = HeroInfo.objects.get(pk = id)
    bookid = hero.book.id
    hero.delete()
    return redirect(reverse('booktest:detail',args=(bookid,)))



