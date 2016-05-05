from django.forms import ModelForm  
from view.models import post_jianzhi  
from django import forms
from django.contrib.admin import widgets


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






class ExamInfoForm(ModelForm):  
	title = forms.CharField(max_length=30)
	jian_jie = forms.CharField(max_length=300,widget=forms.Textarea(attrs={'id':'txt_introduction'}))
	jing_er = forms.IntegerField()
	di_zhi = forms.CharField(max_length=30)
	shi_jian = forms.CharField(max_length=10,widget=widgets.AdminDateWidget())	
	shi_jian2 = forms.CharField(max_length=10,widget=widgets.AdminDateWidget())	
	lxfs = forms.CharField(max_length=50)
	area = forms.ChoiceField(widget = forms.Select(),choices=ZS_AREA)
	day_hw = forms.ChoiceField(choices=CHOICE_DAY_HW)
	zhao_ping = forms.IntegerField()
	jie_suan = forms.ChoiceField(choices=CHOICE_jie_suan)

	class Meta:
		model = post_jianzhi
		fields = ('__all__')
