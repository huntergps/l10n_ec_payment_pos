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
