# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    qualification_ids = fields.One2many(string='Qualifications', comodel_name='hr.applicant.qualification', inverse_name='applicant_id')
    formation_ids = fields.One2many(string='Formation', comodel_name='hr.applicant.formation', inverse_name='applicant_id')
    aptitude_ids = fields.One2many(string='Aptitudes', comodel_name='hr.applicant.aptitude', inverse_name='applicant_id')
    job_qualification_ids = fields.One2many(string='Qualifications Requise', related='job_id.qualification_ids', comodel_name='hr.job.qualification')
    job_aptitude_ids = fields.One2many(string='Qualifications Requise', related='job_id.aptitude_ids', comodel_name='hr.job.aptitude')
    job_formation_ids = fields.One2many(string='Formations necessaire', related='job_id.formation_ids', comodel_name='hr.job.formation')
