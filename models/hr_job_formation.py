# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_job_formation(osv.osv):

    _name = "hr.job.formation"
    _description = "Formation requis pour le poste"

    _columns = {
        'name':fields.many2one('hr.employee.formation.module', 'Formation'),
        'job_id':fields.many2one('hr.job', 'Poste'),
    }
hr_job_formation()
