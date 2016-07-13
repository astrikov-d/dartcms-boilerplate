# coding: utf-8
from django.conf.urls import include, url
from django.views.i18n import javascript_catalog

js_info_dict = {
    'packages': ('app',),
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),

    url(r'^', include('app.home.urls', namespace='home')),
]
