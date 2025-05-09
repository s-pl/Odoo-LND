from odoo import models, fields, api

class Departamento(models.Model):
    _name = 'empleados.departamento'
    _description = 'Departamento'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)
    presupuesto = fields.Float(string='Presupuesto Anual')
    activo = fields.Boolean(string='Activo', default=True)
    empleado_ids = fields.One2many('empleados.empleado', 'departamento_id', string='Empleados')
    notas = fields.Text(string='Notas')

class Empleado(models.Model):
    _name = 'empleados.empleado'
    _description = 'Empleado'

    name = fields.Char(string='Nombre', required=True)
    numero_empleado = fields.Char(string='Número de Empleado', required=True)
    departamento_id = fields.Many2one('empleados.departamento', string='Departamento', required=True)
    fecha_contratacion = fields.Date(string='Fecha de Contratación')
    salario = fields.Float(string='Salario')
    pedido_ids = fields.One2many('ventas.pedido', 'vendedor_id', string='Pedidos')
    total_ventas = fields.Float(string='Total de Ventas', compute='_compute_total_ventas', store=True)
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('vacaciones', 'Vacaciones'),
        ('baja', 'Baja')
    ], string='Estado', default='activo')

    @api.depends('pedido_ids.total')
    def _compute_total_ventas(self):
        for empleado in self:
            empleado.total_ventas = sum(pedido.total for pedido in empleado.pedido_ids)