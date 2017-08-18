# -*- coding: utf-8 -*-


from openerp import models
from openerp.osv import fields, osv
import datetime

class hr_employee(osv.osv):
        _inherit = 'hr.employee'

        def _wb(self, cr, uid, ids, field_name, arg, context):
            employees = self.read(cr, uid, ids, ['birthday', 'id'], context)
            res = {}
            for employee in employees:
                if employee['birthday']:
                    res[employee['id']] = datetime.datetime.strptime(employee['birthday'], "%Y-%m-%d").strftime("%W")
            return res
        def _seniority(self, cr, uid, ids, field_name, arg, context):
            employees = self.read(cr, uid, ids, ['date', 'id'])
            res = {}
            for employee in employees:
                days = datetime.datetime.now() - datetime.datetime.strptime(employee['date'], '%Y-%m-%d')
                avgyear = 365.2425  # pedants definition of a year length with leap years
                avgmonth = 365.2425 / 12.0  # even leap years have 12 months
                years, remainder = divmod(days.days, avgyear)
                years, months = int(years), int(remainder // avgmonth)
                m, d = divmod(remainder, avgmonth)
                seniority = str(years) + ' ans, ' + str(months) + ' mois, ' + str(int(d)) + ' jours.'
                res[employee['id']] = seniority
            return res

        def _preavis(self, cr, uid, ids, field_name, arg, context):
            groups = ['Groupe I', 'Groupe II', 'Groupe III', 'Groupe IV', 'Groupe V']
            employees = self.read(cr, uid, ids, ['category_ids', 'date', 'id'], context)
            res = {}
            grid = {}
            grid[1] = {'Groupe I':1, 'Groupe II':2, 'Groupe III':3, 'Groupe IV':4, 'Groupe V':5}
            grid[2] = {'Groupe I':3, 'Groupe II':8, 'Groupe III':15, 'Groupe IV':30, 'Groupe V':30}
            grid[3] = {'Groupe I':8, 'Groupe II':2, 'Groupe III':3, 'Groupe IV':4, 'Groupe V':5}
            grid[4] = {'Groupe I':10, 'Groupe II':30, 'Groupe III':45, 'Groupe IV':75, 'Groupe V':120}
            grid[5] = {'Groupe I':30, 'Groupe II':45, 'Groupe III':60, 'Groupe IV':90, 'Groupe V':180}
            preavis = 0
            categ_obj = self.pool.get('hr.employee.category')

            for employee in employees:
                if employee['date']:
                    days = datetime.datetime.now() - datetime.datetime.strptime(employee['date'], '%Y-%m-%d')
                    days_employed = days.days
                    years = round(days_employed / 365)
                    if employee['category_ids']:
                        categ_id = employee['category_ids'][0]
                    else:
                        res[employee['id']] = 9999
                        continue
                    category = categ_obj.browse(cr, uid, categ_id)
                    if category != []:
                        category = category.parent_id.name
                    else:
                        category = 'N/A'
                    if category not in groups:
                        res[employee['id']] = 9999
                        continue
                    if years >= 5:
                        preavis = grid[5][category]
                    elif years >= 3:
                        preavis = grid[4][category] + (years * 2)
                    elif years >= 1:
                        preavis = grid[4][category]
                    else:
                        if days_employed < 8:
                            preavis = grid[1][category]
                        elif days_employed < 90:
                            preavis = grid[2][category]
                        else:
                            preavis = grid[3][category]
                    res[employee['id']] = preavis
            return res

        _columns = {
            'children_ids': fields.one2many('hr.employee.children',
                                            'employee_id', 'Enfants'),
            'mother': fields.char('Mere', size=64),
            'father': fields.char('Pere', size=64),
            'spouse': fields.char('Epoux(se)', size=64),

            'weekbirthday':fields.function(_wb, method=True, string='Week Birthday', type='char'),
            'preavis':fields.function(_preavis, method=True, string='Preavis', type='float'),
            'seniority':fields.function(_seniority, method=True, string='Anciennete', type='char'),
            'sanction_ids':fields.one2many('hr.employee.sanction', 'name', 'Sanctions'),
            'qualification_ids':fields.one2many('hr.employee.qualification', 'employee_id', 'Qualifications'),
            'medical_ids':fields.one2many('hr.employee.medical.ticket', 'employee_id', 'Billet Medical'),
            'decoration_ids':fields.one2many('hr.employee.decoration', 'employee_id', 'Decorations'),  # add by Hari
            'note_ids':fields.one2many('hr.employee.note', 'employee_id', 'Note Employe'),  # add by Hari
                    'lastjob_ids':fields.one2many('hr.employee.last.job', 'employee_id', 'Ancien Emploie'),  # add by Hari
            'formation_ids':fields.one2many('hr.employee.formation', 'employee_id', 'Formation'),  # add by Hari
        }
hr_employee()


class hr_employee(models.Model):

    _inherit = 'hr.employee'

    manager_user_id = fields.Many2one('res.users', related='parent_id.user_id')
