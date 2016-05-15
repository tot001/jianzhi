#-*- coding: UTF-8 -*-  
from django.db import models
from django.forms import ModelForm
import time
ZS_AREA = (
    ('石岐','石岐'),
    ('东区','东区'),
    ('西区','西区'),
    ('南区','南区'),
    ('五桂山','五桂山'),
    ('火炬开发区','火炬开发区'),
    ('黄埔','黄埔'),
    ('南头','南头'),
    ('东凤','东凤'),
    ('阜沙','阜沙'),
    ('小榄','小榄'),
    ('东升','东升'),
    ('古镇','古镇'),
    ('横栏','横栏'),
    ('三角','三角'),
    ('民众','民众'),
    ('南朗','南朗'),
    ('港口','港口'),
    ('大涌','大涌'),
    ('沙溪','沙溪'),
    ('三乡','三乡'),
    ('板芙','板芙'),
    ('神湾','神湾'),
    ('坦洲','坦洲'),
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
