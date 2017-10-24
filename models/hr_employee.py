# -*- coding: utf-8 -*-


from openerp import api, exceptions, fields, models, _
import datetime
import logging
logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    # def _get_chargefam(self, cr, uid, ids, field_name, arg, context):
    #     employees = self.browse(cr, uid, ids)
    #     res = {}
    #     for employee in employees:
    #         count = 0
    #         for child in employee.children_ids:
    #             ages = child.age.split()
    #             if len(ages) > 1:
    #                 if int(ages[0][:-1]) < 21:
    #                     count += 1
    #         res[employee.id] = count
    #     return res

    @api.multi
    def _get_chargefam(self):
        for emp in self:
            ages_list = emp.mapped('children_ids.age')
            emp.chargefam = sum(int(age.split('a')[0]) < 21 for age in ages_list)

    @api.multi
    def _get_visibility(self):
        user_obj = self.env['res.users']
        for emp in self:
            uid = self._uid
            visible = False
            group_ids = user_obj.browse(uid).groups_id
            group_user_id_user = self.env.ref('base.group_hr_user')
            group_user_id_manager = self.env.ref('base.group_hr_manager')
            if (group_user_id_user.id in [group.id for group in group_ids]) or (group_user_id_manager.id in [group.id for group in group_ids]) \
               or (emp.user_id.id == uid) or (emp.parent_id.user_id.id == uid):
                visible = True
            emp.visible = visible

    @api.multi
    def _wb(self):
        for emp in self:
            if emp.birthday:
                emp.weekbirthday = datetime.datetime.strptime(emp.birthday, "%Y-%m-%d").strftime("%W")

    # TODO
    def attendance_action_change(self, cr, uid, ids, context=None):
        if not context:
            return {}
        return False

    @api.multi
    def _get_children(self):
        """
            Get number of all children for an employee
        """
        for emp in self:
            emp.children = len(emp.children_ids)

    matricule = fields.Char(string='Matricule', size=64)
    cin = fields.Char(string='CIN', size=64)
    cin_date = fields.Date(string='Date CIN')
    cin_place = fields.Char(string='Lieu CIN', size=30)
    chargefam = fields.Float(string='Charge Familliale', compute='_get_chargefam')
    visible = fields.Boolean(string='Visible',compute='_get_visibility')
    payment_term_id = fields.One2many(string='Mode de Paiement',comodel_name='payment.term',inverse_name='employee_id')
    anciennete = fields.Boolean(string='Prime anciennete',help=u'Est ce que cet employe benificie de la prime d\'anciennete')
    affilie = fields.Boolean(string='Affilie',help=u'Est ce qu\'on va calculer les cotisations pour cet employe')
    state = fields.Selection(string='State', selection=[('absent', 'Absent'), ('present', 'Present')], default='absent')
    children_ids = fields.One2many(string='Enfants', comodel_name='hr.employee.children', inverse_name='employee_id')
    mother = fields.Char(string='Mere', size=64)
    father = fields.Char(string='Pere', size=64)
    spouse = fields.Char(string='Epoux(se)', size=64)
    weekbirthday = fields.Char(string='Week Birthday', compute='_wb')
    sanction_ids = fields.One2many(string='Sanctions', comodel_name='hr.employee.sanction', inverse_name='name')
    qualification_ids = fields.One2many(string='Qualifications', comodel_name='hr.employee.qualification', inverse_name='employee_id')
    medical_ids = fields.One2many(string='Billet Medical', comodel_name='hr.employee.medical.ticket', inverse_name='employee_id')
    decoration_ids = fields.One2many(string='Decorations', comodel_name='hr.employee.decoration', inverse_name='employee_id')
    note_ids = fields.One2many(string='Note Employe', comodel_name='hr.employee.note', inverse_name='employee_id')
    lastjob_ids = fields.One2many(string='Ancien Emploie', comodel_name='hr.employee.last.job', inverse_name='employee_id')
    formation_ids = fields.One2many(string='Formation', comodel_name='hr.employee.formation', inverse_name='employee_id')
    aptitude_ids = fields.One2many(string='Aptitudes', comodel_name='hr.employee.aptitude', inverse_name='employee_id')
    #contract_ids = fields.One2many(string='Contrats',comodel_name='hr.contract',inverse_name='employee_id')
    children = fields.Integer(string=u'Number of childs',compute='_get_children')
