from odoo import models, fields, api

class ProductoInventario(models.Model):
    _name = 'inventario.producto'
    _description = 'Producto de Inventario'

    name = fields.Char(string='Nombre del Producto', required=True)
    codigo = fields.Char(string='Código', required=True)
    precio_venta = fields.Float(string='Precio de Venta', required=True, default=0.0)
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado'),
        ('bajo_stock', 'Bajo Stock')
    ], string='Estado', default='disponible')
    cantidad = fields.Integer(string='Cantidad', default=1)
    notas = fields.Text(string='Notas')
    activo = fields.Boolean(string='Activo', default=True)

    @api.onchange('cantidad')
    def _onchange_cantidad(self):
        if self.cantidad <= 0:
            self.estado = 'agotado'
        elif self.cantidad < 5:
            self.estado = 'bajo_stock'
        else:
            self.estado = 'disponible'

    _sql_constraints = [
        ('codigo_unico', 'UNIQUE(codigo)',
         'Ya existe un producto con este código')
    ]
