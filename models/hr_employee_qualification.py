# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_qualification(osv.osv):
    """gestion des qualifications"""
    _name = 'hr.employee.qualification'
    _columns = {
    'date': fields.date('Date'),
    'name': fields.many2one('qual.type', 'Qualification'),
    'employee_id':fields.many2one('hr.employee', 'Salarie'),
        'branche_id':fields.many2one('hr.employee.branche', 'Branche'),  # #add by Hari
        'specialite':fields.char('Specialite', size=16),  # #add by Hari
        'annee':fields.integer('Annee'),  # #add by Hari
        'lieu':fields.char('Lieu', size=32),  # #add by Hari

    }
hr_employee_qualification()
