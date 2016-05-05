#-*- coding: UTF-8 -*-  
from django.db import models
from django.forms import ModelForm
import time
ZS_AREA = (
    ('sq','石岐'),
    ('dq','东区'),
    ('xq','西区'),
    ('nq','南区'),
    ('wgs','五桂山'),
    ('hjkfq','火炬开发区'),
    ('hp','黄埔'),
    ('nt','南头'),
    ('df','东凤'),
    ('fs','阜沙'),
    ('xl','小榄'),
    ('ds','东升'),
    ('gz','古镇'),
    ('hl','横栏'),
    ('sj','三角'),
    ('mz','民众'),
    ('nl','南朗'),
    ('gk','港口'),
    ('dz','大涌'),
    ('sha_xi','沙溪'),
    ('san_xiang','三乡'),
    ('bf','板芙'),
    ('sw','神湾'),
    ('tz','坦洲'),
)



CHOICE_DAY_HW = (
    ('元/天','元/天'),
    ('元/时','元/时'),
)


CHOICE_jie_suan= (
    ('完工结算','完工结算'),
    ('每天结算','每天结算'),
    ('每周结算','每周结算'),
    ('每月结算','每月结算'),

)

class post_jianzhi(models.Model):
    title = models.CharField(max_length=30,blank=False)
    jian_jie = models.CharField(max_length=300,blank=False)
    jing_er = models.IntegerField(blank=False)
    di_zhi = models.CharField(max_length=30,blank=False)
    shi_jian = models.CharField(max_length=10,blank=False)
    shi_jian2 = models.CharField(max_length=10,blank=False)
    lxfs = models.CharField(max_length=50,blank=False)
    timer =  models.DateTimeField(auto_now_add=True)
    area = models.CharField(max_length=30,blank=False,choices=ZS_AREA)
    day_hw = models.CharField(max_length=10,blank=False,choices=CHOICE_DAY_HW)
    zhao_ping = models.IntegerField(blank=False)
    jie_suan = models.CharField(max_length=10,blank=False,choices=CHOICE_jie_suan)
    


    
     
    def __str__(self):# 在Python2中用 __unicode__  代替 __str__
        return str(self.title) + str(self.jing_er) + str(self.area) + str(self.timer) +str(self.jian_jie)+str(self.lxfs)+str(self.di_zhi)+str(self.shi_jian2)+str(self.shi_jian)
