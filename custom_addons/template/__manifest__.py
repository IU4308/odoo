{
    'name': 'Template',
    'version': '1.0',
    'category': 'Forms Builder',
    'summary': "View aggregated results for user's template",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/import_template_wizard_view.xml',
        'data_import/template_actions.xml',
        'views/template_form_views.xml',
        'views/template_menus.xml',
    ],  
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}