# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_last_job(osv.osv):
    """Gestion des anciens emploie des employes"""
    _name = 'hr.employee.last.job'
    _columns = {
    'employee_id':fields.many2one('hr.employee', 'Employe'),
        'annee':fields.char('Annee',size=16),
        # #'poste':fields.selection((('a','A'),('b','B'),('b+','B+'),('c','C'),('c+','C+'),('d','D')),'Note'),
        'poste':fields.char('Poste', size=32),
        'employeur':fields.char('Employeur', size=32),
        'ref':fields.char('Reference', size=32),
        'ordre':fields.integer('Ordre'),
        'date_start':fields.date('Debut'),
    'date_stop':fields.date('Fin'),

    }
hr_employee_last_job()
