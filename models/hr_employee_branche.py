# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrEmployeeBranche(models.Model):
    """gestion des branches des qualifications"""
    _name = 'hr.employee.branche'
    
    code = fields.Char( string = 'Code Branche', size=16)
    name = fields.Char(string = 'Nom Branche', size=64)
    niveau = fields.Integer(string = 'Niveau')
