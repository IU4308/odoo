
{
    'name': 'Estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage estate properties',
    'depends': ['base'],
    'data': [
        'data/ir.model.access.csv', 
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
    ],  
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
