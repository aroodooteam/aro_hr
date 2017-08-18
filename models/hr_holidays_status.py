# -*- coding: utf-8 -*-

from openerp import models, api, fields
import logging
_logger = logging.getLogger(__name__)


class hr_holidays_status(models.Model):

    _inherit = "hr.holidays.status"

    @api.multi
    def get_days(self, employee_id, context=None):
        result = dict((holiday.id,
                       dict(max_leaves=0, leaves_taken=0, remaining_leaves=0,
                            virtual_remaining_leaves=0)) for holiday in self)
        ids = []
        for holiday in self:
            ids.append(holiday.id)
        holiday_ids = self.env['hr.holidays'].search(
            [('employee_id', '=', employee_id),
             ('state', 'in', ['confirm', 'validate1', 'validate']),
             ('holiday_status_id', 'in', ids)])
        accounted = []
        for holiday in holiday_ids:
            status_dict = result[holiday.holiday_status_id.id]
            nb_dtmp = holiday.number_of_days_temp
            if holiday.type == 'add':
                status_dict['virtual_remaining_leaves'] += nb_dtmp
                if holiday.state == 'validate':
                    status_dict['max_leaves'] += nb_dtmp
                    status_dict['remaining_leaves'] += nb_dtmp
            elif holiday.type == 'remove':  # number of days is negative
                status_dict['virtual_remaining_leaves'] -= nb_dtmp
                if holiday.state == 'validate':
                    status_dict['leaves_taken'] += holiday.number_of_days_temp
                    status_dict['remaining_leaves'] -= nb_dtmp
            if holiday.holiday_status_id.id not in accounted and \
               holiday.holiday_status_id.anciennete:
                accounted.append(holiday.holiday_status_id.id)
                employee = self.env['hr.employee'].search(
                    [('id', '=', employee_id)])
                seniority = employee.seniority.split(' ')
                if ('mois,') in seniority:
                    seniority.remove('mois,')
                if ('jours') in seniority:
                    seniority.remove('jours')
                if ('ans,') in seniority:
                    seniority.remove('ans,')
                months = int(seniority[1])
                to_exclude = 0
                for hol in employee.job_id.hr_holiday_job_ids:
                    if hol.name == holiday.holiday_status_id:
                        to_exclude = hol.days * months
                status_dict['max_leaves'] -= to_exclude
        return result

    weekend = fields.Boolean('Ouvrable')
    days = fields.Float('Jours à attribuer')
    frequency = fields.Selection(
        [('monthly', 'Mensuel'), ('yearly', 'Annuel')], 'Attribution')
    reset = fields.Boolean(u'Reinitialisation annuel')
    global_holiday = fields.Boolean(
        u'Congé commun', help='Definition pas necessaire dans le poste')
    anciennete = fields.Boolean(u'Attribution sur ancienneté')
