# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class medical_type(osv.osv):
        _name = 'medical.type'
        _columns = {
                'name':fields.char('Description', size=32),
                'detail':fields.text('Text sur document'),
        }
medical_type()
