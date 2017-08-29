# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrEmployeeLastJob(models.Model):
    """Gestion des anciens emploie des employes"""

    _name = 'hr.employee.last.job'

    employee_id = fields.Many2one(string='Employe',comodel_name='hr.employee')
    annee = fields.Char(string=u'Année',size=16)
    poste = fields.Char(string='Poste',size=32)
    employeur = fields.Char(string='Employeur',size=32)
    ref = fields.Char(string='Reference',size=32)
    ordre = fields.Integer(string='Ordre')
    date_start = fields.Date(string='Debut')
    date_stop = fields.Date(string='Fin')

