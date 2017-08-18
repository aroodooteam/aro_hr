# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime


class hr_task_categ(osv.osv):
    _name = 'hr.task.categ'

    _columns = {
        'name':fields.char('Catégorie')
    }
hr_task_categ()
