# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models,


class HrEmployeeMedicalTicket(models.Model):
    """gestion des ticket medical"""
    _name = 'hr.employee.medical.ticket'
    _description = "Employee Medical Ticket"

    
        date = fields.Datetime(string = 'Date')
        name = fields.Many2one(comodel_name = 'medical.type', string = 'Medical')
        repos = fields.Boolean(string = 'Avec repos')
        date_debut_repos = fields.Date( string = 'Date debut repos')
        date_fin_repos = fields.Date(string = 'Date reprise de poste')
        employee_id = fields.Many2one(comodel_name ='hr.employee', string = 'Salarie')
    
HrEmployeeMedicalTicket()


