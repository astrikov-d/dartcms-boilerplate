# coding: utf-8
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'home/index.html'