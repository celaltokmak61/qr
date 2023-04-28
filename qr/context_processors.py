# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from constance import config


def site_info(request):
    return {
        'INSTAGRAM': config.INSTAGRAM,
        'EMAIL': config.EMAIL
    }
