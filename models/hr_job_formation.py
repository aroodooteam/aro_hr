# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrJobFormation(models.model):
	_name = "hr.job.formation"
    _description = "Formation requis pour le poste"

    name = fields.Many2one(comodel_name='hr.employee.formation.module', 'Formation')
    job_id = fields.Many2one(comodel_name='hr.job', 'Poste')

