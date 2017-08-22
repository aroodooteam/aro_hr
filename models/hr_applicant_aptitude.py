# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrApplicantAptitude(models.Model):
	_name = 'hr.applicant.aptitude'
 	_description = 'Aptitudes d'un employe'

	name = fields.many2one('aptitude.type', 'Aptitude')
	applicant_id=fields.many2one('hr.applicant','Candidat')
 	taux=fields.integer(u'Taux amployé %')
