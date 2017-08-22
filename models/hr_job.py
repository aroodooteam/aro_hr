# -*- coding:  utf-8 -*-
##############################################################################
#
#    OpenERP,  Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http: //tiny.be>).
#
#    This program is free software:  you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation,  either version 3 of the
#    License,  or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not,  see <http: //www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields


# import datetime

from openerp import models, api, exceptions
import logging

_logger = logging.getLogger(__name__)


class hr_job(models.Model):
    _inherit = "hr.job"

    _columns = {
        'qualification_ids':fields.one2many('hr.job.qualification', 'job_id', 'Qualification Requises'),
        'formation_ids':fields.one2many('hr.job.formation', 'job_id', 'Formations Requises'),
        'aptitude_ids':fields.one2many('hr.job.aptitude', 'job_id', 'Aptitudes Technique'),
        'time_start':fields.char('Heure Debut', size=5),
        'time_stop':fields.char('Heure Fin', size=5),
        'internal_relation':fields.text('Relation interne'),
        'external_relation':fields.text('Relation externe'),
        'task_ids':fields.one2many('hr.job.task', 'job_id', 'Taches'),
        }

    @api.multi
    def create_survey(self):
        self.ensure_one()
        plan_obj = self.env['hr_evaluation.plan']
        survey_obj = self.env['survey.survey']
        page_obj = self.env['survey.page']
        employee_obj = self.env['hr.employee']
        evaluation_obj = self.env['hr_evaluation.evaluation']
        name = 'Evaluation' + ' ' + self.name
        result = plan_obj.search([('name', '=', name)])
        if not result:
            technical_survey = survey_obj.search(
                [('title', '=', 'Evaluation Technique ' + self.name)])
            if technical_survey:
                technical_survey_id = technical_survey[0].id
            else:
                questions = []
                if not self.task_ids:
                    raise exceptions.Warning(
                        'Aucune tache defini pour ce poste')
                for task in self.task_ids:
                    questions.append((0, 0, {'value': task.name}))
                survey_data = {
                    'title': 'Evaluation Technique ' + self.name,
                    'users_can_go_back': True,
                    'auth_required': True,
                    'res_model': 'hr_evaluation',
                    'quizz_mode': True,
                    }
                _logger.info(survey_data)
                technical_survey_id = survey_obj.create(survey_data)
                _logger.info(technical_survey_id)
                page_id = page_obj.create(
                    {'survey_id': technical_survey_id.id,
                     'title': 'Evaluation Technique ' + self.name,
                     'question_ids': [
                         (0, 0,
                          {'question': 'Evaluation Technique ' + self.name,
                           'type': 'matrix',
                           'constr_mandatory': True,
                           'constr_error_msg': 'Reponse Obligatoire',
                           'comments_allowed': False,
                           'labels_ids': [
                               (0, 0, {'value': '5', 'quizz_mark': 20}),
                               (0, 0, {'value': '4', 'quizz_mark': 16}),
                               (0, 0, {'value': '3', 'quizz_mark': 12}),
                               (0, 0, {'value': '2', 'quizz_mark': 8}),
                               (0, 0, {'value': '1', 'quizz_mark': 4})
                           ],
                           'labels_ids_2':  questions})]}
                )
                _logger.info(page_id)
            plan_data = {
                'name':  name,
                'phase_ids': [
                    # (0, 0,
                    # {'name': 'Technique', 'action': 'top-down',
                    # 'survey_id': }),
                    (0, 0,
                     {'name': u'Générique',
                      'action': 'top-down',
                      'survey_id': survey_obj.search(
                          [('title', '=', u'Evaluation Génériques')])[0].id}),
                    (0, 0,
                     {'name': u'Globale',
                      'action': 'top-down',
                      'survey_id': survey_obj.search(
                          [('title', '=', u'Evaluation Globale')])[0].id}),
                    (0, 0, {
                            'name': u'Technique',
                            'action': 'top-down',
                            'survey_id': technical_survey_id.id})
                    ]
            }
            plan_id = plan_obj.create(plan_data)
            employees = employee_obj.search([('job_id', '=', self.id)])
            for employee in employees:
                evaluation = evaluation_obj.create(
                    {'employee_id': employee.id,
                        'plan_id': plan_id.id})
                evaluation.button_plan_in_progress()
        else:
            raise exceptions.Warning("Plan d'evaluation existe pour ce poste")

# Fusionner ces 2 classes hr_job dans une seule classe


class hr_job(models.Model):
    _inherit = 'hr.job'

    hr_holiday_job_ids = fields.One2many('hr.holiday.job', 'job_id', 'Conges')
    replacement = fields.Boolean('Remplacement Obligatoire')