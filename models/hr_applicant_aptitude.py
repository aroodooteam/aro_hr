# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_applicant_aptitude(osv.osv):

    _name = "hr.applicant.aptitude"
    _description = "Aptitudes d'un employe"

    _columns = {
        'name':fields.many2one('aptitude.type', 'Aptitude'),
        'applicant_id':fields.many2one('hr.applicant', 'Candidat'),
        'taux':fields.integer(u'Taux employé %'),
        }
hr_applicant_aptitude()
