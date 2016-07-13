# coding: utf-8
from dartcms import get_dartcms_core_apps

PROJECT_APPS = [
    'app'
] + get_dartcms_core_apps()

PROJECT_AUTHENTICATION_BACKENDS = []

PROJECT_TEMPLATE_CONTEXT_PROCESSORS = ['dartcms.context_processors.modules_data']

PROJECT_MIDDLEWARE_CLASSES = []

RAVEN_CONFIG = {}
