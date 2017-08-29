# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrEmployeeFormation(models.Model):
    """Gestion des formations des employes chez ARO"""

    _name = 'hr.employee.formation'
    _description = u'Formations'

    _rec_name = 'name'
    _order = 'name ASC'
    ref = fields.Integer(string='Reference')
    employee_id = fields.Many2one(string='Employe',comodel_name='hr.employee')
    date = fields.Date(string='Date')
    module_id = fields.Many2one(string='Module',comodel_name='hr.employee.formation.module')
    commentaire = fields.Text(string='Commentaire')
    name = fields.Many2one(string='Qualification',comodel_name='qual.type')
    branche_id = fields.Many2one(string='Niveau',comodel_name='hr.employee.branche')
    specialite = fields.Char(string='Specialite',size=64)
    institute_id = fields.Many2one(string='Institut',comodel_name='institute')
    lieu = fields.Char(string='Lieu',size=64)