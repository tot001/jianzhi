#-*- coding: UTF-8 -*-  
from django.shortcuts import render
from django.http import HttpResponse
from view.models import post_jianzhi
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
import os.path
import datetime
import time

# Create your views here.
def index(request):
            limit = 20
            objects = post_jianzhi.objects.all()[::-1]

            p = Paginator(objects,limit)
            page = request.GET.get('page')
            
            try:
                db = p.page(page)
            except PageNotAnInteger:
                db = p.page(1)
            except EmptyPage:
                db = p.page(p.num_pages);

              

            return render(request, 'index2.html',{'db': db})


        


#各区过滤
def sq(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sq"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})

def dq(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="dq"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})

def xq(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="xq"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})

def nq(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nq"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def wgs(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="wgs"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def hjkfq(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hjkfq"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def hp(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hp"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def nt(request):        
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nt"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def df(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="df"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def fs(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="fs"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def xl(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="xl"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def ds(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="ds"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def gz(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="gz"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def hl(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hl"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def sj(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sj"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def mz(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="mz"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def nl(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nl"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def gk(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="gk"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def dc(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="dc"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def sha_xi(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sha_xi"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def san_xiang(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="san_xiang"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def bf(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="bf"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def sw(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sw"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})
def tz(request):
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="tz"))[::-1]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index2.html',{'db':db})





#搜索
def search(request):
        limit = 20
        kw = request.GET['user_search']
        page = request.GET.get('page')
        objects = post_jianzhi.objects.filter(Q(title__icontains=kw)|Q(jian_jie__icontains=kw)|Q(di_zhi__icontains=kw))[::-1]
        p = Paginator(objects,limit)
        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'index.html',{'db':db,'kw':kw})





def inside_view(request):
        page = request.GET['in']
        db = post_jianzhi.objects.filter(id=page)
        return render(request,'content.html',{ 'db':db })



