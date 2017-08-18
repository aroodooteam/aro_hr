# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_medical_ticket(osv.osv):
    """gestion des ticket medical"""
    _name = 'hr.employee.medical.ticket'
    _columns = {
        'date': fields.datetime('Date'),
        'name': fields.many2one('medical.type', 'Medical'),
        'repos': fields.boolean('Avec repos'),
        'date_debut_repos': fields.date('Date debut repos'),
        'date_fin_repos': fields.date('Date reprise de poste'),
        'employee_id':fields.many2one('hr.employee', 'Salarie'),
    }
hr_employee_medical_ticket()
