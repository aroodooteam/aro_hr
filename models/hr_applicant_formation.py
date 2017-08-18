# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_applicant_formation(osv.osv):
    """Gestion des formations des employes chez ARO"""
    _name = 'hr.applicant.formation'
    _description = 'Formations'
    _columns = {
        'ref':fields.integer('Reference'),
        'applicant_id':fields.many2one('hr.applicant', 'Candidat'),
        'date':fields.date('Date'),
        'name':fields.many2one('hr.employee.formation.module', 'Formation'),
        'commentaire':fields.text('Commentaire'),
    }
hr_applicant_formation()
