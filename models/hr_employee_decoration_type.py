# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_decoration_type(osv.osv):
    """gestion des types de decoration existant chez ARO."""
    _name = 'hr.employee.decoration.type'
    _columns = {
        'code': fields.char('Code Decoration', size=16),
        'name':fields.char('Titre Decoration', size=64),
    }
hr_employee_decoration_type()
