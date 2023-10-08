# -*- coding: utf-8 -*-
{
    'name': 'Estate',
    'website': 'https://www.facebook.com/dev.Phuong2711/',
    'summary': 'Estate',
    'author': 'Sonbn',
    'version': '16.0.1.2',
    'license': 'LGPL-3',
    'support ': 'Dev.Phuong2711@gmail.com',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'th_pagoda/static/src/js/*.js',
        #     'th_pagoda/static/src/xml/*.xml',
        #     'th_pagoda/static/src/scss/*.scss',
        #
        # ],
    },
    'installable': True,
    'application': True,
}
