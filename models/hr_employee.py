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

    def _get_chargefam(self, cr, uid, ids, field_name, arg, context):
        employees = self.browse(cr, uid, ids)
        res = {}
        for employee in employees:
            count = 0
            for child in employee.children_ids:
                ages = child.age.split()
                if len(ages) > 1:
                    if int(ages[0][:-1]) < 21:
                        count += 1
            res[employee.id] = count
        return res

    def _get_visibility(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for emp in self.browse(cr, uid, ids, context=context):
            visible = False
            if emp.user_id.id == uid:
                visible = True
            elif emp.parent_id.user_id.id == uid:
                visible = True
            else:
                group_ids = self.pool.get('res.users').browse(
                    cr, uid, uid, context=context).groups_id
                group_user_id = self.pool.get("ir.model.data").get_object_reference(cr, uid, 'base', 'group_hr_user')[1]
                if group_user_id in [group.id for group in group_ids]:
                    visible = True
                else:
                    group_user_id = self.pool.get("ir.model.data").get_object_reference(cr, uid, 'base', 'group_hr_manager')[1]
                    if group_user_id in [group.id for group in group_ids]:
                        visible = True
            res[emp.id] = visible
        return res

    # TODO
    def attendance_action_change(self, cr, uid, ids, context=None):
        if not context:
            return {}
        return False

    _columns = {
        'matricule': fields.char('Matricule', size=64),
        'cin': fields.char('CIN', size=64),
        'cin_date': fields.date('Date CIN'),
        'cin_place': fields.char('Lieu CIN', size=30),
        'working_hours': fields.many2one('resource.calendar',
                                         'Working Schedule'),
        'chargefam': fields.function(_get_chargefam, method=True, type='float'),
        'visible': fields.function(_get_visibility, method=True,
                                   string='Visible', type='boolean'),
        'payment_term_id': fields.one2many('payment.term', 'employee_id',
                                           'Mode de Paiement'),
        'anciennete': fields.boolean('Prime anciennete', help='Est ce que cet employe benificie de la prime d\'anciennete'),
        'affilie': fields.boolean(
            'Affilie',
            help='Est ce qu\'on va calculer les cotisations pour cet employe'),
        'state': fields.selection([('absent', 'Absent'), ('present', 'Present')], 'State'),

        'children_ids': fields.one2many('hr.employee.children',
                                        'employee_id', 'Enfants'),
        'mother': fields.char('Mere', size=64),
        'father': fields.char('Pere', size=64),
        'spouse': fields.char('Epoux(se)', size=64),

        'weekbirthday':fields.function(_wb, method=True, string='Week Birthday', type='char'),
        'sanction_ids':fields.one2many('hr.employee.sanction', 'name', 'Sanctions'),
        'qualification_ids':fields.one2many('hr.employee.qualification', 'employee_id', 'Qualifications'),
        'medical_ids':fields.one2many('hr.employee.medical.ticket', 'employee_id', 'Billet Medical'),
        'decoration_ids':fields.one2many('hr.employee.decoration', 'employee_id', 'Decorations'),  # add by Hari
        'note_ids':fields.one2many('hr.employee.note', 'employee_id', 'Note Employe'),  # add by Hari
        'lastjob_ids':fields.one2many('hr.employee.last.job', 'employee_id', 'Ancien Emploie'),  # add by Hari
        'formation_ids':fields.one2many('hr.employee.formation', 'employee_id', 'Formation'),  # add by Hari

        'aptitude_ids':fields.one2many('hr.employee.aptitude', 'employee_id', 'Aptitudes'),
    }
    _defaults = {
        'state': 'absent'
    }

hr_employee()


# class hr_employee(models.Model):
# 
#     _inherit = 'hr.employee'
# 
#     manager_user_id = fields.Many2one('res.users', related='parent_id.user_id')
