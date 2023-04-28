# -*- coding: utf-8 -*-

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_ADDITIONAL_FIELDS = {
    'shelf_restriction': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (
            ("", "---"), ("same_barcode", "Only Same Barcode"), ("same_size", "Only Same Sizes"), ("all", "All"))
    }],
}
CONSTANCE_CONFIG = {
<<<<<<< Updated upstream
    'FOOTER_TEXT': ('Bu sayfa bir günlük otağı projesidir.', 'footer text'),
    'KEYWORDS': ('chat gpt makale, chatgpt, chatmakale, makale botu', 'keywords'),
    'SITE_NAME': ('ChatGPT Makale', 'site name'),
    'SITE_DESCRIPTION': ('ChatGPT Makale Botu, otomatik makale yazdır', 'site description'),
    'OPENAI_KEY': ('', 'OpenAi Key'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'GENERAL OPTIONS': (
        'FOOTER_TEXT',
        'KEYWORDS',
        'SITE_NAME',
        'SITE_DESCRIPTION',
        'OPENAI_KEY'
=======
    'INSTAGRAM': ('', 'instagram profile url'),
    'EMAIL': ('', 'email contact'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'SOCIAL MEDIA': (
        'INSTAGRAM',
        'EMAIL'
>>>>>>> Stashed changes
    ),
}