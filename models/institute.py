# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class institute(osv.osv):
    _name = 'institute'
    _columns = {
        'name':fields.char('Institut'),
    }
institute()
