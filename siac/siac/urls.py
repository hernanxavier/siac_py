from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siac.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^sistema/', include(admin.site.urls)),

    url(r'^registro/', include('apps.sistema.urls'), name='registro'),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    url(r'^$', 'django.contrib.auth.views.login',
        {'template_name': 'sistema/login.html'}, name='login'),
)
