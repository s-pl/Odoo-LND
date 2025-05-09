{
    'name': 'Gestión de Ventas',
    'description': 'Módulo para gestionar pedidos y líneas de pedido',
    'version': '1.0',
    'summary': 'Gestión de ventas',
    'category': 'Sales',
    'author': 'Samuel Ponce Luna',
    'depends': ['base', 'inventario'],
    'data': [
        'security/ir.model.access.csv',
        'views/ventas_views.xml',
    ],
    'installable': True,
    'application': True
}