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

def ajax_index(request):
            objects = post_jianzhi.objects.all()[::-20]
            limit = len(objects)
            p = Paginator(objects,limit)
            page = request.GET.get('page')
            
            try:
                db = p.page(page)
            except PageNotAnInteger:
                db = p.page(1)
            except EmptyPage:
                db = p.page(p.num_pages);

            return render(request, 'ajax.html',{'db': db})











def ajax_sq(request):
        ajax = sq
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
        return render(request,'ajax.html',{'db':db,'ajax':ajax})

def ajax_dq(request):
        ajax = dq
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="dq"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})

def ajax_xq(request):
        ajax = xq
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="xq"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})

def ajax_nq(request):
        ajax = nq
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nq"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_wgs(request):
        ajax = wgs
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="wgs"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_hjkfq(request):
        ajax = hjkfq
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hjkfq"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_hp(request):
        ajax = hp
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hp"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_nt(request):        
        ajax = nt
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nt"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_df(request):
        ajax = df
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="df"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_fs(request):
        ajax = fs
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="fs"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_xl(request):
        ajax = xl
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="xl"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_ds(request):
        ajax = ds
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="ds"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_gz(request):
        ajax = gz
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="gz"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_hl(request):
        ajax = hl
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="hl"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_sj(request):
        ajax = sj
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sj"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_mz(request):
        ajax = mz
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="mz"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_nl(request):
        ajax = nl
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="nl"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_gk(request):
        ajax = gk
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="gk"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_dc(request):
        ajax = dc
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="dc"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_sha_xi(request):
        ajax = sha_xi
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sha_xi"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_san_xiang(request):
        ajax = san_xiang
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="san_xiang"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_bf(request):
        ajax = bf
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="bf"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_sw(request):
        ajax = sw
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="sw"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})
def ajax_tz(request):
        ajax = tz
        limit = 20
        objects = list(post_jianzhi.objects.filter(area__exact="tz"))[::-20]
        p = Paginator(objects,limit)
        page = request.GET.get('page')

        try:
            db = p.page(page)
        except PageNotAnInteger:
            db = p.page(1)
        except EmptyPage:
            db = p.page(p.num_pages);
        return render(request,'ajax.html',{'db':db,'ajax':ajax})















        


#各区过滤
# def sq(request):
#         limit = 2
#         objects = list(post_jianzhi.objects.filter(area__exact="sq"))[::-1]
#         p = Paginator(objects,limit)
#         page = request.GET.get('page')

#         try:
#             db = p.page(page)
#         except PageNotAnInteger:
#             db = p.page(1)
#         except EmptyPage:
#             db = p.page(p.num_pages);
#         return render(request,'index2_sq.html',{'db':db})

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
        return render(request,'index2_dq.html',{'db':db})

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
        return render(request,'index2_xq.html',{'db':db})

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
        return render(request,'index2_nq.html',{'db':db})
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
        return render(request,'index2_wgs.html',{'db':db})
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
        return render(request,'index2_hjkfq.html',{'db':db})
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
        return render(request,'index2_hp.html',{'db':db})
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
        return render(request,'index2_nt.html',{'db':db})
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
        return render(request,'index2_df.html',{'db':db})
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
        return render(request,'index2_fs.html',{'db':db})
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
        return render(request,'index2_xl.html',{'db':db})
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
        return render(request,'index2_ds.html',{'db':db})
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
        return render(request,'index2_gz.html',{'db':db})
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
        return render(request,'index2_hl.html',{'db':db})
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
        return render(request,'index2_sj.html',{'db':db})
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
        return render(request,'index2_mz.html',{'db':db})
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
        return render(request,'index2_nl.html',{'db':db})
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
        return render(request,'index2_gk.html',{'db':db})
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
        return render(request,'index2_dc.html',{'db':db})
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
        return render(request,'index2_sha_xi.html',{'db':db})
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
        return render(request,'index2_san_xiang.html',{'db':db})
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
        return render(request,'index2_bf.html',{'db':db})
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
        return render(request,'index2_sw.html',{'db':db})
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
        return render(request,'index2_tz.html',{'db':db})





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



