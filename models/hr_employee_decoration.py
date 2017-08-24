# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _

class ModelName(models.Model):
    """gestion des decorations de l'employé"""

    _name = 'hr.employee.decoration'
    _description = u'decorations de l\'employé %'

    annee = fields.Date(string='Date')
    decoration_id = fields.Many2one(string='Titre Decoration',comodel_name='hr.employee.decoration.type')
    employee_id = fields.Many2one(string='Salarié',comodel_name='hr.employee')