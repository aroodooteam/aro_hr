# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class aptitude_type(osv.osv):

    _name = "aptitude.type"
    _description = "Type D'aptitude"

    _columns = {
        'name':fields.char('Aptitude', size=64),
        }
aptitude_type()
