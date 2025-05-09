from odoo import models, fields, api

class Pedido(models.Model):
    _name = 'ventas.pedido'
    _description = 'Pedido de Venta'

    name = fields.Char(string='Número de Pedido', required=True)
    fecha_pedido = fields.Date(string='Fecha de Pedido', default=fields.Date.today)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado')
    ], string='Estado', default='borrador')
    cliente = fields.Char(string='Cliente', required=True)
    notas = fields.Text(string='Notas')
    linea_ids = fields.One2many('ventas.linea_pedido', 'pedido_id', string='Líneas de Pedido')
    vendedor_id = fields.Many2one('empleados.empleado', string='Vendedor', ondelete='set null')
    direccion_entrega = fields.Text(string='Dirección de Entrega')
    metodo_pago = fields.Selection([
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia')
    ], string='Método de Pago', default='efectivo')
    fecha_entrega = fields.Date(string='Fecha de Entrega Estimada')
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('linea_ids.subtotal')
    def _compute_total(self):
        for pedido in self:
            pedido.total = sum(linea.subtotal for linea in pedido.linea_ids)

class LineaPedido(models.Model):
    _name = 'ventas.linea_pedido'
    _description = 'Línea de Pedido'

    pedido_id = fields.Many2one('ventas.pedido', string='Pedido', required=True, ondelete='cascade')
    producto_id = fields.Many2one('inventario.producto', string='Producto', required=True, ondelete='restrict')
    name = fields.Char(string='Descripción', related='producto_id.name', store=True, readonly=True)
    cantidad = fields.Integer(string='Cantidad', default=1)
    precio_unitario = fields.Float(string='Precio Unitario', digits=(10, 2))
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True, digits=(10, 2))

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for linea in self:
            linea.subtotal = linea.cantidad * linea.precio_unitario

    @api.onchange('producto_id')
    def _onchange_producto(self):
        if self.producto_id:
            self.precio_unitario = self.producto_id.precio_venta
        else:
            self.precio_unitario = 0.0