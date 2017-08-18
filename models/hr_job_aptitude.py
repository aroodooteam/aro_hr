# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_job_aptitude(osv.osv):

    _name = "hr.job.aptitude"
    _description = "Aptitude necessaire pour un poste"

    _columns = {
        'name':fields.many2one('aptitude.type', 'Aptitude Requis'),
        'job_id':fields.many2one('hr.job', 'Poste'),
        'taux':fields.integer('Taux requis'),
        }
hr_job_aptitude()
