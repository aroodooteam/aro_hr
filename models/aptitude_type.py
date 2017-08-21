# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

# =================Version v7=====================
# from openerp.osv import fields, osv
# import datetime


# class aptitude_type(osv.osv):
# 
#     _name = "aptitude.type"
#     _description = "Type D'aptitude"
# 
#     _columns = {
#         'name':fields.char('Aptitude', size=64),
#         }
# aptitude_type()


# =================Version v8=================


class AptitudeType(models.Model):
    _name = 'aptitude.type'
    _description = "Type D'aptitude"

    name = fields.Char(string='Aptitude', size=64)
