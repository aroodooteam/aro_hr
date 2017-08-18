# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_branche(osv.osv):
    """gestion des branches des qualifications"""
    _name = 'hr.employee.branche'
    _columns = {
    'code': fields.char('Code Branche', size=16),
        'name':fields.char('Nom Branche', size=64),
        'niveau':fields.integer('Niveau'),
    }
hr_employee_branche()
