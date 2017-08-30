# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models


class MedicalType(models.Model):
        _name = 'medical.type'
        _description = "Medical Type"

        name = fields.Char(string = 'Description', size=32)
        detail = fields.Text(string = 'Text sur document')
