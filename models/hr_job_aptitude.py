# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrJobAptitude(models.Model):

    _name = "hr.job.aptitude"
    _description = "Aptitude necessaire pour un poste"

    name = fields.Many2one(comodel_name='aptitude.type', string='Aptitude Requis')
    job_id = fields.Many2one(comodel_name='hr.job', string='Poste')
    taux = fields.Integer(string='Taux requis')
