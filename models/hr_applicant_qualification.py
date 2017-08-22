# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class hr_applicant_qualification(models.Model):
    """ gestion des qualifications  """

    _name = 'hr.applicant.qualification'
    _description = 'Qualification'

    date = fields.Datetime(string='Date')
    name = fields.Many2one(string='Qualification',comodel_name='qual.type')
    applicant_id = fields.Many2one(string='Candidat',comodel_name='hr.applicant')
    branche_id = fields.Many2one(string='Branche',comodel_name='hr.employee.branche')
    specialite = fields.Char(string='Specialite',size=16)
    annee = fields.Integer(string='Annee')
    lieu = fields.Char(string='Lieu',size=32)
