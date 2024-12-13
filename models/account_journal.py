# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2004-2008 PC Solutions (<http://pcsol.be>). All Rights Reserved
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    # pos_payment_method_id = fields.Many2one(
    #     'pos.payment.method',
    #     string='Metodo de Pago',
    #     index=True
    # )
    #
    # @api.constrains('pos_payment_method_id')
    # def _check_journal_payment_method(self):
    #     for record in self:
    #         if record.pos_payment_method_id and record.company_id != record.pos_payment_method_id.company_id:
    #             raise ValidationError(_("El diario debe pertenecer a la misma compañía que el método de pago."))
