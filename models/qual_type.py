# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class qual_type(osv.osv):
    _name = 'qual.type'
    _columns = {
        'name':fields.char('Description'),
        'code':fields.char(u'Code diplôme', size=16),
    }
qual_type()
