# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime

class sanction_type(osv.osv):
        _name = 'sanction.type'
        _columns = {
                'name':fields.char('Description', size=64),
                'detail':fields.text('Text sur document'),
                'interview':fields.boolean('Entretiens?'),
                'notification':fields.boolean('Notification?'),
                'days_work':fields.boolean('A defalquer sur jours travailles?'),

        }
sanction_type()
