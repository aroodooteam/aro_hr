# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class QualType(models.Model):
    _name = 'qual.type'

    name = fields.Char(string='Description')
    code = fields.Char(string=u'Code diplôme', size=16)
