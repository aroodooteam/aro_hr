# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_note(osv.osv):
    """Gestion des notes des employes"""
    _name = 'hr.employee.note'
    _columns = {
    'employee_id':fields.many2one('hr.employee', 'Employe'),
        'annee':fields.char('Annee', size=16),
        'note':fields.selection((('a', 'A'), ('b', 'B'), ('b+', 'B+'), ('c', 'C'), ('c+', 'C+'), ('d', 'D')), 'Note'),
        'mois':fields.char('Mois', size=32),
        'ref':fields.char('Reference', size=32),
    }
hr_employee_note()
