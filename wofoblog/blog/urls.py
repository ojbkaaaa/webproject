"""wofoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from blog import views
from django.conf.urls import handler404, handler500



app_name = 'blog'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^commit/$', views.commit, name='commit'),
    url(r'^detail/(?P<pk>[0-9]+)', views.detail,name='detail'),
    url(r'^index/$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact , name='contact'),
    url(r'^login/$', views.login, name='login'),
    url(r'^user_info/$', views.user_info, name='user_info'),
    url(r'^put/$', views.put, name='put'),
    url(r'^out/$', views.out, name='out'),
#    url(r'^register/$', views.register, name='register'),
    url(r'^add/$', views.add, name='add'),
    url(r'comments', include('comments.urls')),
    url(r'item', views.item, name='item'),
    # url(r'^find/$', views.find, name='find'),
    # url(r'^image/$', views.image, name='image'),
    url(r'^imageupdate/$', views.imageupdate, name='imageupdate'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tagview, name='tagview'),

]
handler404 = views.page_not_found
handler500 = views.page_error
