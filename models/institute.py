# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class Institute(models.Model):
    _name = 'institute'
    _descritpion = "institute"

    name = fields.Char(string='Institute')