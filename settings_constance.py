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
    'TWITTER': ('', 'twitter profile url'),
    'EMAIL': ('', 'email adress'),
    'NUMBER': ('', 'phone number'),
    'FACEBOOK': ('', 'facebook profile url'),
    'ADDRESS': ('', 'address'),
    'INSTAGRAM': ('', 'instagram profile url'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'SOCIAL MEDIA': (
        'TWITTER',
        'FACEBOOK',
        'INSTAGRAM'
    ),
     'CONTACT': (
        'NUMBER',
        'EMAIL',
        'ADDRESS',
    ),
}