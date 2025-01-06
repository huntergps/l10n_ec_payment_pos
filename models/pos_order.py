# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _, tools

from odoo.tools import float_compare, float_is_zero, format_date
import psycopg2
from odoo.osv.expression import AND
from collections import defaultdict
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def sync_from_ui(self, orders):
        for order in orders:
            print(order)
        result = super().sync_from_ui(orders)
        return result



    @api.model_create_multi
    def create(self, vals_list):
        res = super(PosOrder, self).create(vals_list)
        for rec in res:
            if rec.seller_pos_id:
                rec.seller_user_id = rec.seller_pos_id
            if rec.employee_pos_id:
                rec.employee_user_id = rec.employee_pos_id
        return res
