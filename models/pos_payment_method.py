from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    payment_type = fields.Selection([('cash', 'Efectivo'), ('bank', 'Transaccion Bancaria'),
        ('card', 'Tarjeta'), ('credit', 'Credito'), ('advance', 'Anticipo'), ('cross', 'Cruce de Cartera')],
        'Tipo de Pago', default='cash')


    allowed_journal_ids = fields.One2many(
        'pos.payment.method.journal',  # Nombre del modelo intermedio
        'pos_payment_method_id',  # Campo que se relaciona con el método de pago
        string='Diarios Permitidos'
    )

    serialized_allowed_journals = fields.Json(
        string="Diarios Permitidos Serializados",
        compute="_compute_serialized_allowed_journals",
        store=True
    )


    def _is_write_forbidden(self, fields):
        print(fields)
        whitelisted_fields = {'name','sequence','allowed_journal_ids','payment_type',
            'l10n_ec_sri_payment_id','outstanding_account_id','journal_id'}
        return bool(fields - whitelisted_fields and self.open_session_ids)

    def get_allowed_journals(self):
        """Devuelve los diarios permitidos como registros de account.journal."""
        return self.allowed_journal_ids.mapped('journal_id')

    @api.depends('allowed_journal_ids.journal_id')
    def _compute_serialized_allowed_journals(self):
        for record in self:
            record.serialized_allowed_journals = [
                {'id': journal.journal_id.id, 'name': journal.journal_id.name}
                for journal in record.allowed_journal_ids
            ]

    @api.model
    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id)
        res += ['serialized_allowed_journals','payment_type']
        return res


class PosPaymentMethodJournal(models.Model):
    _name = 'pos.payment.method.journal'  # Modelo intermedio
    _description='Diarios para Pagos de POS'
    
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
            if record.pos_payment_method_id.company_id != record.journal_id.company_id:
                raise ValidationError(_("El diario debe pertenecer a la misma compañía que el método de pago."))
