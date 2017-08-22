# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrApplicantAptitude(models.Model):
    _name = 'hr.applicant.aptitude'
    _description = '''Aptitudes d'un employe'''

    name = fields.Many2one(string='Aptitude', comodel_name='aptitude.type')
    applicant_id = fields.Many2one(string='Candidat', comodel_name='hr.applicant')
    taux = field_name = fields.Integer(string= u'Taux employé %')
