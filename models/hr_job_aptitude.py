# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrJobAptitude(models.model):

    _name = "hr.job.aptitude"
    _description = "Aptitude necessaire pour un poste"

    name = fields.Many2one(string='aptitude.type', 'Aptitude Requis')
    job_id = fields.Many2one(string='hr.job', 'Poste')
    taux = fields.Integer(string='Taux requis')
