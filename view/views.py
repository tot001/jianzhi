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

# 首页
def index(request):
            # limit = 20
            objects = post_jianzhi.objects.all()[::-1]
            db = objects[:20]
            forajax = "index"

            # p = Paginator(objects,limit)
            # page = request.GET.get('page')    p.page(1)
    
            # except PageNotAnInteger:
            #     db = p.page(1)
            # except EmptyPage:
            #     db = p.page(p.num_pages);

            return render(request, 'index_ajax.html',{'db': db,'forajax':forajax})


#aJax 首页
def ajax_index(request):
            objects = post_jianzhi.objects.all()[::-1]
            db = objects[20:]
            if len(db) == 0:
                return render(request,'EmptyPage.html')
            else:
                return render(request, 'ajax.html',{'db': db})

            # except PageNotAnInteger:
            #     db = p.page(1)
            # except EmptyPage:
            #     db = p.page(p.num_pages);

            








#ajax 区域
def ajax_sq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="石岐"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})

def ajax_dq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东区"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})

def ajax_xq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="西区"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})

def ajax_nq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南区"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_wgs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="五桂山"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_hjkfq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="火炬开发区"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_hp(request):
        objects = list(post_jianzhi.objects.filter(area__exact="黄埔"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_nt(request):        
        objects = list(post_jianzhi.objects.filter(area__exact="南头"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_df(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东凤"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_fs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="阜沙 "))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_xl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="小榄"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_ds(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东升"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_gz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="古镇"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_hl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="横栏"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_sj(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三角"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_mz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="民众"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_nl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南朗"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_gk(request):
        objects = list(post_jianzhi.objects.filter(area__exact="港口"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_dc(request):
        objects = list(post_jianzhi.objects.filter(area__exact="大涌"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_sha_xi(request):
        objects = list(post_jianzhi.objects.filter(area__exact="沙溪"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_san_xiang(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三乡"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_bf(request):
        objects = list(post_jianzhi.objects.filter(area__exact="板芙"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_sw(request):
        objects = list(post_jianzhi.objects.filter(area__exact="神湾"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})
def ajax_tz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="坦洲"))[::-1]
        db = objects[20:]
        if len(db) == 0:
            return render(request,'EmptyPage.html')
        else:
            return render(request, 'ajax.html',{'db': db})













        


#各区过滤
def sq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="石岐"))[::-1]
        db = objects[:20]
        forajax = "sq"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})

def dq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东区"))[::-1]
        db = objects[:20]
        forajax = "dq"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})

def xq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="西区"))[::-1]
        db = objects[:20]
        forajax = "xq"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})

def nq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南区"))[::-1]
        db = objects[:20]
        forajax = "nq"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def wgs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="五桂山"))[::-1]
        db = objects[:20]
        forajax = "wgs"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def hjkfq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="火炬开发区"))[::-1]
        db = objects[:20]
        forajax = "hjkfq"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def hp(request):
        objects = list(post_jianzhi.objects.filter(area__exact="黄埔"))[::-1]
        db = objects[:20]
        forajax = "hp"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def nt(request):        
        objects = list(post_jianzhi.objects.filter(area__exact="南头"))[::-1]
        db = objects[:20]
        forajax = "nt"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def df(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东凤"))[::-1]
        db = objects[:20]
        forajax = "df"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def fs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="阜沙"))[::-1]
        db = objects[:20]
        forajax = "fs"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def xl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="小榄"))[::-1]
        db = objects[:20]
        forajax = "xl"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def ds(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东升"))[::-1]
        db = objects[:20]
        forajax = "ds"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def gz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="古镇"))[::-1]
        db = objects[:20]
        forajax = "gz"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def hl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="横栏"))[::-1]
        db = objects[:20]
        forajax = "hl"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def sj(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三角"))[::-1]
        db = objects[:20]
        forajax = "sj"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def mz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="民众"))[::-1]
        db = objects[:20]
        forajax = "mz"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def nl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南朗"))[::-1]
        db = objects[:20]
        forajax = "nl"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def gk(request):
        objects = list(post_jianzhi.objects.filter(area__exact="港口"))[::-1]
        db = objects[:20]
        forajax = "gk"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def dc(request):
        objects = list(post_jianzhi.objects.filter(area__exact="大涌"))[::-1]
        db = objects[:20]
        forajax = "dc"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def sha_xi(request):
        objects = list(post_jianzhi.objects.filter(area__exact="沙溪"))[::-1]
        db = objects[:20]
        forajax = "sha_xi"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def san_xiang(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三乡"))[::-1]
        db = objects[:20]
        forajax = "san_xiang"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def bf(request):
        objects = list(post_jianzhi.objects.filter(area__exact="板芙"))[::-1]
        db = objects[:20]
        forajax = "bf"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def sw(request):
        objects = list(post_jianzhi.objects.filter(area__exact="神湾"))[::-1]
        db = objects[:20]
        forajax = "sw"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
def tz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="坦洲"))[::-1]
        db = objects[:20]
        forajax = "tz"
        return render(request,'index_ajax.html',{'db':db,'forajax':forajax})
 





























#搜索
def search(request):
        forajax = "search"
        kw = request.GET['user_search']
        objects = post_jianzhi.objects.filter(Q(title__icontains=kw)|Q(jian_jie__icontains=kw)|Q(di_zhi__icontains=kw))[::-1]
        db = objects[:20]
        return render(request,'index.html',{'db':db,'forajax':forajax,'kw':kw})
 

#ajax 搜索
def ajax_search(request):
        kw = request.GET['user_search']
        objects = post_jianzhi.objects.filter(Q(title__icontains=kw)|Q(jian_jie__icontains=kw)|Q(di_zhi__icontains=kw))[::-1]
        db = objects[20:]
        if len(db) == 0 :
            return render(request,'EmptyPage.html')
        else:
            return render(request,'ajax.html',{'db':db})

























#内容
def inside_view(request):
        page = request.GET['in']
        db = post_jianzhi.objects.filter(id=page)
        return render(request,'content.html',{ 'db':db })



