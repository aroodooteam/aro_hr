# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrApplicantFormation(models.Model):
    _name = 'hr.applicant.formation'
    _description = 'Formations'

    ref = fields.Integer(string='Reference')
    applicant_id = fields.Many2one(string='Candidat',comodel_name='hr.applicant')
    date = fields.Datetime(string='Date')
    name = fields.Many2one(string='Formation',comodel_name='hr.employee.formation.module')
    commentaire = fields.Text(string='Commentaire')
