# -*- coding: utf-8 -*-
{
    'name': "Analytics label Custom",

    'summary': """
        permite agrupar por etiquetas analiticas en el mayor y en el reporte de análsis de factura""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Gabriela Riquelme",
    'website': "http://www.Exemax.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
      #  'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
