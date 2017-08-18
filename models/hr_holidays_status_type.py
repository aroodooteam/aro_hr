# -*- coding: utf-8 -*-

from openerp import models, api, fields, tools, _
import logging
_logger = logging.getLogger(__name__)


class hr_holidays_status_type(models.Model):

    _name = "hr.holidays.status.type"
    _description = 'Type de permission'
    name = fields.Char('Type de permission')
    limit = fields.Float('Limite')
    proof = fields.Char('Justificatif')
