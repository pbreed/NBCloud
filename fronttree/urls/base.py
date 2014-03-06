from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Home Page -- Replace as you prefer
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'about', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'contact', 'fronttree.views.contact'),

    url(r'reading','fronttree.views.reading'),
    url(r'raw','fronttree.views.readings'),

    url("^datagraph", 'fronttree.views.graphdata'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
