from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'dj_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'shiwenfeng/',views.do_app)
]