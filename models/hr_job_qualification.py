# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_job_qualification(osv.osv):

    _name = "hr.job.qualification"
    _description = "Qualifications Pour un poste"

    _columns = {
    'name': fields.many2one('qual.type', 'Qualification Requise'),
    'branche_id':fields.many2one('hr.employee.branche', 'Branche'),  # #add by Hari
    'specialite':fields.char('Specialite', size=64),  # #add by Hari
    'job_id':fields.many2one('hr.job', 'Poste'),
        }
hr_job_qualification()
