# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models,


class HrEmployeeQualification(models.Model):
    """gestion des qualifications"""
    _name = 'hr.employee.qualification'
    _description = "Employee Qualification" 
    
        date = fields.Date(string = 'Date')
        name = fields.Many2one(comodel_name = 'qual.type', string = 'Qualification')
        employee_id = fields.Many2one( comodel_name ='hr.employee', string = 'Salarie')
        branche_id = fields.Many2one(comodel_name = 'hr.employee.branche', string = 'Branche') # #add by Hari
        specialite = fields.char(string = 'Specialite', size=16) # #add by Hari
        annee = fields.Integer(string = 'Annee') # #add by Hari
        lieu = fields.Char(string= 'Lieu', size=32) # #add by Hari
        institute_id = fields.Many2one('institute', string = 'Institut')
        job_id = fields.Many2one(comodel_name='hr.job', related='employee_id.job_id', string='Poste')
        matricule = fields.Char(related='employee_id.matricule', string ='Matricule', store=True)
    



