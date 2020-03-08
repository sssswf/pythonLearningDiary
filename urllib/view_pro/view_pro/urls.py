from django.conf.urls import include, url
from django.contrib import admin
from student import student_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'view_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/',include(student_url))

]
