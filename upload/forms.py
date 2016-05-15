from django.forms import ModelForm  
from view.models import post_jianzhi  
from django import forms
from django.contrib.admin import widgets


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
