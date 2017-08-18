# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_formation(osv.osv):
    """Gestion des formations des employes chez ARO"""
    _name = 'hr.employee.formation'
    _columns = {
        'ref':fields.integer('Reference'),
    'employee_id':fields.many2one('hr.employee', 'Employe'),
        'date':fields.date('Date'),
        'module_id':fields.many2one('hr.employee.formation.module', 'Module'),
        'code_module':fields.char('Code Module', size=32),  # inutile pour le moment
        'commentaire':fields.text('Commentaire'),
    }
hr_employee_formation()
