# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime

class hr_applicant(osv.osv):
    _inherit = 'hr.applicant'

    _columns = {
        'qualification_ids':fields.one2many('hr.applicant.qualification','applicant_id','Qualifications'),
        'formation_ids':fields.one2many('hr.applicant.formation','applicant_id','Formation'),#add by Hari
        'aptitude_ids':fields.one2many('hr.applicant.aptitude','applicant_id','Aptitudes'),
        'job_qualification_ids':fields.related('job_id','qualification_ids',string='Qualifications Requise',type='one2many',relation='hr.job.qualification'),
        'job_aptitude_ids':fields.related('job_id','aptitude_ids',string='Aptitudes Requise',type='one2many',relation='hr.job.aptitude' ),
        'job_qualification_ids':fields.related('job_id','qualification_ids',string='Qualifications Requise',type='one2many',relation='hr.job.qualification'),
        'job_formation_ids':fields.related('job_id','formation_ids',string='Formations necessaire',type='one2many',relation='hr.job.formation'),
    }
