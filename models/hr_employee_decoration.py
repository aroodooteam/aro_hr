# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_decoration(osv.osv):
    """gestion des decorations de l'employé"""
    _name = 'hr.employee.decoration'
    _columns = {
        # 'code': fields.char('Code Decoration', size=16),
        'annee':fields.date('Date'),
        'decoration_id':fields.many2one('hr.employee.decoration.type', 'Titre Decoration'),
        'employee_id':fields.many2one('hr.employee', 'Salarié'),
   }
hr_employee_decoration()
