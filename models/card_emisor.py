# -*- coding: utf-8 -*-

from odoo import api, fields, models



class CreditCardBrand(models.Model):
    _inherit = "account.credit.card.brand"

    available_in_pos = fields.Boolean(string='Disponible en POS', default=False)

    @api.model
    def _load_pos_data_domain(self, data):
        return [('available_in_pos', '=', True)]

    @api.model
    def _load_pos_data_fields(self, config_id):
        return ['id','name']


    def _load_pos_data(self, data):
        domain = []
        domain = self._load_pos_data_domain(data)
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        data = self.search_read(domain, fields, load=False)
        return {
            'data': data,
            'fields': fields
        }


class CreditCardDeadLine(models.Model):
    _inherit = "account.credit.card.deadline"

    available_in_pos = fields.Boolean(string='Disponible en POS', default=False)

    @api.model
    def _load_pos_data_domain(self, data):
        return [('available_in_pos', '=', True)]

    @api.model
    def _load_pos_data_fields(self, config_id):
        return ['id','name']


    def _load_pos_data(self, data):
        domain = []
        domain = self._load_pos_data_domain(data)
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        data = self.search_read(domain, fields, load=False)
        return {
            'data': data,
            'fields': fields
        }
