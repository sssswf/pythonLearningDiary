from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'dj_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^acu/',tv.do_acu),
    url(r'^ACU/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.do_ACU),
    url(r'^teacher/',include(teacher_url)),
]
