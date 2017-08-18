# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_employee_aptitude(osv.osv):

    _name = "hr.employee.aptitude"
    _description = "Aptitudes d'un employe"

    _columns = {
        'name':fields.many2one('aptitude.type', 'Aptitude'),
        'niveau':fields.char('Niveau'),
        'employee_id':fields.many2one('hr.employee', 'Employe'),
        'taux':fields.integer('Taux employe'),
        }
hr_employee_aptitude()
