from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    allowed_journal_ids = fields.One2many(
        'pos.payment.method.journal',  # Nombre del modelo intermedio
        'pos_payment_method_id',  # Campo que se relaciona con el método de pago
        string='Diarios Permitidos'
    )

    def _is_write_forbidden(self, fields):
        whitelisted_fields = {'sequence','allowed_journal_ids'}
        return bool(fields - whitelisted_fields and self.open_session_ids)


class PosPaymentMethodJournal(models.Model):
    _name = 'pos.payment.method.journal'  # Modelo intermedio

    pos_payment_method_id = fields.Many2one(
        'pos.payment.method', string='Método de Pago'
    )
    journal_id = fields.Many2one(
        'account.journal', string='Diario'
    )
    company_id = fields.Many2one(
        'res.company', related='journal_id.company_id', store=True, string='Compañía'
    )


    @api.constrains('pos_payment_method_id', 'journal_id')
    def _check_journal_payment_method(self):
        for record in self:
            # Validamos que el diario esté asociado a la misma compañía que el método de pago
            if record.pos_payment_method_id.company_id != record.journal_id.company_id:
                raise ValidationError(_("El diario debe pertenecer a la misma compañía que el método de pago."))
