# -*- coding: utf-8 -*-
{
    'name': "Website Layout Customize",

    'summary': """Customize website layout""",

    'description': """
        Customize website layout
    """,

    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_layout_template.xml',
        'views/res_company_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
