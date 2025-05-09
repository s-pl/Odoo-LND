{
    'name': 'Gestión de Empleados',
    'description': 'Módulo para gestionar empleados y departamentos',
    'version': '1.0',
    'summary': 'Gestión de empleados',
    'category': 'Human Resources',
    'author': 'Samuel Ponce Luna',
    'depends': ['base', 'ventas'],
    'data': [
        'security/ir.model.access.csv',
        'views/empleados_views.xml',
    ],
    'installable': True,
    'application': True
}