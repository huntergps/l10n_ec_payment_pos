# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class PosSession(models.Model):
	_inherit = 'pos.session'

	def _load_pos_data_models(self, config_id):
		res = super()._load_pos_data_models(config_id)
		res += ['res.bank','account.journal','account.credit.card.brand','account.credit.card.deadline']
		return res
