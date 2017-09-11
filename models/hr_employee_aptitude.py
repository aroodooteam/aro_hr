# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrEmployeeAptitude(models.Model):

    _name = "hr.employee.aptitude"
    _description = "Aptitudes d'un employe"

    name = fields.Many2one(comodel_name='aptitude.type', string='Aptitude')
    niveau = fields.Char( string='Niveau')
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employe')
    taux = fields.Integer(string='Taux employe')
