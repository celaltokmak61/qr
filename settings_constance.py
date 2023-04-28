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
    'INSTAGRAM': ('', 'instagram profile url'),
    'EMAIL': ('', 'email contact'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'SOCIAL MEDIA': (
        'INSTAGRAM',
        'EMAIL'
    ),
}