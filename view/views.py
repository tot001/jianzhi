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
            ajax = "index"
            forajax = "区域"

            # p = Paginator(objects,limit)
            # page = request.GET.get('page')    p.page(1)
    
            # except PageNotAnInteger:
            #     db = p.page(1)
            # except EmptyPage:
            #     db = p.page(p.num_pages);

            return render(request, 'index_ajax.html',{'db': db,'forajax':forajax,'ajax':ajax})


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
        ajax = "sq"
        forajax = "石岐"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def dq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东区"))[::-1]
        db = objects[:20]
        ajax = "dq"
        forajax = "东区"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def xq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="西区"))[::-1]
        db = objects[:20]
        ajax = "xq"
        forajax = "西区"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})


def nq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南区"))[::-1]
        db = objects[:20]
        ajax = "nq"
        forajax = "南区"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def wgs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="五桂山"))[::-1]
        db = objects[:20]
        ajax = "wgs"
        forajax = "五桂山"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def hjkfq(request):
        objects = list(post_jianzhi.objects.filter(area__exact="火炬开发区"))[::-1]
        db = objects[:20]
        ajax = "hjkfq"
        forajax = "火炬开发区"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def hp(request):
        objects = list(post_jianzhi.objects.filter(area__exact="黄埔"))[::-1]
        db = objects[:20]
        ajax = "hp"
        forajax = "黄埔"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def nt(request):        
        objects = list(post_jianzhi.objects.filter(area__exact="南头"))[::-1]
        db = objects[:20]
        ajax = "nt"
        forajax = "南头"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def df(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东凤"))[::-1]
        db = objects[:20]
        ajax = "df"
        forajax = "东凤"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def fs(request):
        objects = list(post_jianzhi.objects.filter(area__exact="阜沙"))[::-1]
        db = objects[:20]
        ajax = "fs"
        forajax = "阜沙"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def xl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="小榄"))[::-1]
        db = objects[:20]
        ajax = "xl"
        forajax = "小榄"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def ds(request):
        objects = list(post_jianzhi.objects.filter(area__exact="东升"))[::-1]
        db = objects[:20]
        ajax = "ds"
        forajax = "东升"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def gz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="古镇"))[::-1]
        db = objects[:20]
        ajax = "gz"
        forajax = "古镇"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def hl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="横栏"))[::-1]
        db = objects[:20]
        ajax = "hl"
        forajax = "横栏"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def sj(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三角"))[::-1]
        db = objects[:20]
        ajax = "sj"
        forajax = "三角"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def mz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="民众"))[::-1]
        db = objects[:20]
        ajax = "mz"
        forajax = "民众"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def nl(request):
        objects = list(post_jianzhi.objects.filter(area__exact="南朗"))[::-1]
        db = objects[:20]
        ajax = "nl"
        forajax = "南朗"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def gk(request):
        objects = list(post_jianzhi.objects.filter(area__exact="港口"))[::-1]
        db = objects[:20]
        ajax = "gk"
        forajax = "港口"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def dc(request):
        objects = list(post_jianzhi.objects.filter(area__exact="大涌"))[::-1]
        db = objects[:20]
        ajax = "dc"
        forajax = "大涌"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def sha_xi(request):
        objects = list(post_jianzhi.objects.filter(area__exact="沙溪"))[::-1]
        db = objects[:20]
        ajax = "sha_xi"
        forajax = "沙溪"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def san_xiang(request):
        objects = list(post_jianzhi.objects.filter(area__exact="三乡"))[::-1]
        db = objects[:20]
        ajax = "san_xiang"
        forajax = "三乡"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def bf(request):
        objects = list(post_jianzhi.objects.filter(area__exact="板芙"))[::-1]
        db = objects[:20]
        ajax = "bf"
        forajax = "板芙"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def sw(request):
        objects = list(post_jianzhi.objects.filter(area__exact="神湾"))[::-1]
        db = objects[:20]
        ajax = "sw"
        forajax = "神湾"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

def tz(request):
        objects = list(post_jianzhi.objects.filter(area__exact="坦洲"))[::-1]
        db = objects[:20]
        ajax = "tz"
        forajax = "坦洲"
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'index_ajax.html',{'db':db,'forajax':forajax,'ajax':ajax})

 





























#搜索
def search(request):
        kw = request.GET['user_search']
        objects = post_jianzhi.objects.filter(Q(title__icontains=kw)|Q(jian_jie__icontains=kw)|Q(di_zhi__icontains=kw))[::-1]
        db = objects[:20]
        if len(db) < 20:
        	return render(request,'index.html',{'db': db,'forajax':forajax,'ajax':ajax})
        else:
        	return render(request,'search.html',{'db':db,'kw':kw})
 

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



