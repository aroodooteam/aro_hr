# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

#    _columns = {
#        'name':fields.many2one('aptitude.type', 'Aptitude'),
#        'applicant_id':fields.many2one('hr.applicant', 'Candidat'),
#        'taux':fields.integer(u'Taux employé %'),
#        }
#hr_applicant_aptitude()
class hr_applicant_aptitude(models.Model):
	_name = 'hr.applicant.aptitude'
    _description = 'Aptitudes d'un employe'

    #name = fields.Char(string='Aptitude', size=64)
    _name = fields.many2one('aptitude.type', 'Aptitude')
    _applicant_id=fields.many2one('hr.applicant','Candidat')
    _taux=fields.integer(u'Taux amployé %')
