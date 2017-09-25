# -*- coding: utf-8 -*-

from openerp import fields, models, _


class HrEmployeeDecorationType(models.Model):
    """gestion des types de decoration existant chez ARO."""

    _name = 'hr.employee.decoration.type'
    _description = "Decoration"

    code = fields.Char(string='Code', size=16)
    name = fields.Char(string='Title', size=64)
