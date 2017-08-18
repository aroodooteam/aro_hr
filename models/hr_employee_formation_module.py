# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_formation_module(osv.osv):
    """Gestion des modules de formation chez ARO"""
    _name = 'hr.employee.formation.module'
    _columns = {
    'code':fields.char('Code', size=16),
        'name':fields.char('Libellé', size=64),

        # 'cout':fields.float('Coût'), ##champs en stand by
        # 'branche_id':fields.char('Branche',size=16), ##champs en stand by
        # 'specialite':fields.char('Specialite',size=32), ##champs en stand by
    }
hr_employee_formation_module()
