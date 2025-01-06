# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class PosPayment(models.Model):
    _inherit = 'pos.payment'
    payment_type = fields.Selection([('cash', 'Efectivo'), ('bank', 'Transaccion Bancaria'),
        ('card', 'Tarjeta'), ('credit', 'Credito'), ('advance', 'Anticipo'), ('cross', 'Cruce de Cartera')],
        'Tipo de Pago', default='cash')

    transaction_type = fields.Selection([('transf', 'Transferencia'),
        ('desposit', 'Deposito de Efectivo'),('deposit_cheque', 'Deposito de Cheque')],
        'Clase de Transaccion')

    card_type = fields.Selection([('card_credit', 'Tarjeta de Crédito'),
        ('card_debit', 'Tarjeta de Débito')],
        'Clase de Tarjeta')
    transaction_date = fields.Datetime(string='Fecha Transacción', default=lambda self: fields.Datetime.now(), help="Número de comprobante de la transacción bancaria")
    journal_id = fields.Many2one('account.journal', string="Diario Seleccionado", help="Diario seleccionado para este pago")
    journal_ids_allowed = fields.Many2many('account.journal', compute='_compute_journal_ids_allowed', string='Diarios Permitidos')
    bank_id = fields.Many2one('res.bank',string="Banco Origen")
    bank_id_code = fields.Char()
    bank_account_no = fields.Char(string='Nro de Cuenta')
    bank_account_owner_name = fields.Char(string='Dueño de la Cuenta')

    card_brand_id = fields.Many2one('account.credit.card.brand',string="Marca de Tarjeta")
    card_brand_id_code = fields.Char()

    card_deadline_id = fields.Many2one('account.credit.card.deadline',string="Plazo de Tarjeta")
    card_deadline_id_code = fields.Char()


    @api.depends('payment_method_id')
    def _compute_journal_ids_allowed(self):
        for rec in self:
            if rec.payment_method_id:
                rec.journal_ids_allowed = rec.payment_method_id.get_allowed_journals()
            else:
                rec.journal_ids_allowed = self.env['account.journal']

    def get_journal_options(self):
        """Obtiene los diarios permitidos desde el método de pago."""
        return self.payment_method_id.get_allowed_journals() if self.payment_method_id else self.env['account.journal']
