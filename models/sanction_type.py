# -*- coding: utf-8 -*-


from openerp import api, exceptions, fields, models, _
class sanction_type(models.Model):

    _name = 'sanction.type'
    _description = u'Sanction '

    name = fields.Char(string='Description',size=64)
    detail = fields.Text(string='Text sur document')
    interview = fields.Boolean(string='Entretiens?',default=False,)
    notification = fields.Boolean(string='Notification?')
    days_work = fields.Boolean(string='A defalquer sur jours travailles?')
