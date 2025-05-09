{
    'name': 'Inventario realizado por Samuel Ponce Luna',
    'description': 'Módulo de gestión de inventario para Odoo',
    'version': '1.0',
    'summary': 'Gestión de inventario',
    'category': 'Inventory',
    'author': 'Samuel Ponce Luna',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventario_views.xml',
    ],
    'installable': True,
    'application': True,
}
