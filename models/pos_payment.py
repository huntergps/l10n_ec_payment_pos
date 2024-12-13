# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class PosPayment(models.Model):
    _inherit = 'pos.payment'
    
    transaction_date = fields.Datetime(string='Fecha Transacción', default=lambda self: fields.Datetime.now(), help="Número de comprobante de la transacción bancaria")
    journal_id = fields.Many2one('account.journal', string="Diario Seleccionado", help="Diario seleccionado para este pago")

    journal_ids_allowed = fields.Many2many('account.journal', compute='_compute_journal_ids_allowed', string='Diarios Permitidos')

    @api.depends('payment_method_id')
    def _compute_journal_ids_allowed(self):
        for rec in self:
            if rec.payment_method_id:
                # Buscamos los diarios permitidos a través del payment_method_id
                allowed_journal_ids = rec.payment_method_id.allowed_journal_ids
                # Asignamos esos diarios al campo journal_ids_allowed
                rec.journal_ids_allowed = allowed_journal_ids
            else:
                rec.journal_ids_allowed = self.env['account.journal']
