from django.conf.urls import patterns, include, url
from settings import PROJECT_ROOT_PATH
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"),{'template': 'index.html'} ),
    url(r'^home',login_required(TemplateView.as_view(template_name="home.html")),{ 'template': 'index.html' }),
    url(r'^sistema/',include('sistema.url.url_nologin')),
    url(r'^sistema/',include('sistema.url.url_personal')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PROJECT_ROOT_PATH + '/static'}),
    url(r'resources/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PROJECT_ROOT_PATH + '/static'}),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PROJECT_ROOT_PATH + '/static'}),
)
