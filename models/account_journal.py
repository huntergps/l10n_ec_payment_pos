# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2004-2008 PC Solutions (<http://pcsol.be>). All Rights Reserved
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _load_pos_data_domain(self, data):
        return []


    @api.model
    def _load_pos_data_fields(self, config_id):
        return ['id','name']


    def _load_pos_data(self, data):
        domain = []
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        data = self.search_read(domain, fields, load=False)
        return {
            'data': data,
            'fields': fields
        }


class ResBank(models.Model):
    _inherit = 'res.bank'

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
