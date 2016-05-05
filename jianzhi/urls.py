"""text URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from view import views as view_views
from upload import views as upload_views
urlpatterns = [
    url(r'^$',view_views.index), 
    

    url(r'^admin/', admin.site.urls),
    


    url(r'^sq/',view_views.sq),
    url(r'^dq/',view_views.dq),
    url(r'^xq/',view_views.xq),
    url(r'^nq/',view_views.nq),
    url(r'^wgs/',view_views.wgs),
    url(r'^hjkfq/',view_views.hjkfq),
    url(r'^hp/',view_views.hp),
    url(r'^nt/',view_views.nt),
    url(r'^df/',view_views.df),
    url(r'^fs/',view_views.fs),
    url(r'^xl/',view_views.xl),
    url(r'^ds/',view_views.ds),
    url(r'^gz/',view_views.gz),
    url(r'^hl/',view_views.hl),
    url(r'^sj/',view_views.sj),
    url(r'^mz/',view_views.mz),
    url(r'^nl/',view_views.nl),
    url(r'^gk/',view_views.gk),
    url(r'^dc/',view_views.dc),
    url(r'^sha_xi/',view_views.sha_xi),
    url(r'^san_xiang/',view_views.san_xiang),
    url(r'^bf/',view_views.bf),
    url(r'^sw/',view_views.sw),
    url(r'^tz/',view_views.tz),


    url(r'^search/',view_views.search),
    # url(r'^search/$',vie_viebaiws.search_page
    # url(r'^\d+/search',inside_view_views.inside_view),

    
    
    url(r'^upload/',upload_views.get_name),

    

    url(r'^in/',view_views.inside_view),


    # url(r'^sq/\d+/',inside_view_views.sq),
    # url(r'^dq/\d+/',inside_view_views.dq),
    # url(r'^xq/\d+/',inside_view_views.xq),
    # url(r'^nq/\d+/',inside_view_views.nq),
    # url(r'^wgs/\d+/',inside_view_views.wgs),
    # url(r'^hjkfq/\d+/',inside_view_views.hjkfq),
    # url(r'^hp/\d+/',inside_view_views.hp),
    # url(r'^nt/\d+/',inside_view_views.nt),
    # url(r'^df/\d+/',inside_view_views.df),
    # url(r'^fs/\d+/',inside_view_views.fs),
    # url(r'^xl/\d+/',inside_view_views.xl),
    # url(r'^ds/\d+/',inside_view_views.ds),
    # url(r'^gz/\d+/',inside_view_views.gz),
    # url(r'^hl/\d+/',inside_view_views.hl),
    # url(r'^sj/\d+/',inside_view_views.sj),
    # url(r'^mz/\d+/',inside_view_views.mz),
    # url(r'^nl/\d+/',inside_view_views.nl),
    # url(r'^gk/\d+/',inside_view_views.gk),
    # url(r'^dc/\d+/',inside_view_views.dc),
    # url(r'^sha_xi/\d+/',inside_view_views.sha_xi),
    # url(r'^san_xiang/\d+/',inside_view_views.san_xiang),
    # url(r'^bf/\d+/',inside_view_views.bf),
    # url(r'^sw/\d+/',inside_view_views.sw),
    # url(r'^tz/\d+/',inside_view_views.tz),

]
