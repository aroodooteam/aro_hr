# -*- coding: utf-8 -*-

from openerp import models, api, fields, tools, _
import logging
_logger = logging.getLogger(__name__)


class HrReplacement(models.Model):

    _name = 'hr.replacement'

    employee_id = fields.Many2one(string=u'Remplaçant', comodel_name='hr.employee')
    name = fields.Many2one(string=u'Congé', comodel_name='hr.holidays')
    date_start = fields.Datetime('Debut')
    date_stop = fields.Datetime('Fin')
    replace_employee_id = fields.Many2one('hr.employee', related='name.employee_id')
    replace_department_id = fields.Many2one('hr.department', related='replace_employee_id.department_id')
