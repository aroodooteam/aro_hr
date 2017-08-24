# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrEmployeeDecorationType(models.Model):
    """gestion des types de decoration existant chez ARO."""

    _name = 'hr.employee.decoration.type'

    code = fields.Char(string='Code Decoration',size=16)
    name = fields.Char(string='Titre Decoration',size=16)