# -*- coding: utf-8 -*-
{
    'name': "Library Managements",

    'summary': """
        Library Managements""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/groups.xml',
        #'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_book_category_view.xml',
    ],
    'installable': True,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}