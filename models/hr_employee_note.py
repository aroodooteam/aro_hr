# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models,


class HrEmployeeNote(models.Model):
    """Gestion des notes des employes"""
    _name = 'hr.employee.note'
    _description = "Employee Note"
    
        employee_id = fields.Many2one( comodel_name = 'hr.employee', string = 'Employe'),
        annee = fields.Char( string = 'Annee', size=16),
        note = fields.Selection((('a', 'A'), ('b', 'B'), ('b+', 'B+'), ('c', 'C'), ('c+', 'C+'), ('d', 'D')), string = 'Note'),
        mois = fields.Char(string = 'Mois', size=32),
        ref = fields.Char( string = 'Reference', size=32),
    


