# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrJobAptitude(models.model):

    _name = "hr.job.aptitude"
    _description = "Aptitude necessaire pour un poste"

    name = fields.Many2one(comodel_name='aptitude.type', 'Aptitude Requis')
    job_id = fields.Many2one(comodel_name='hr.job', 'Poste')
    taux = fields.Integer(string='Taux requis')
