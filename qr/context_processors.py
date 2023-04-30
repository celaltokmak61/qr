# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from constance import config


def site_info(request):
    return {
        'NUMBER': config.NUMBER,
        'EMAIL': config.EMAIL,
        'FACEBOOK': config.FACEBOOK,
        'TWITTER': config.TWITTER,
        'ADDRESS': config.ADDRESS,
        'INSTAGRAM': config.INSTAGRAM,
        'SITENAME': config.SITENAME,
        'CONTEXT': config.CONTEXT,
        'SLOGAN': config.SLOGAN,
    }
