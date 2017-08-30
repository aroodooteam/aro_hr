# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class PaymentMode(models.Model):

    _name = "payment.mode"
    _description = "Mode de payement"

    code = fields.Char(string='Code', size=8)
    name = fields.Char(string='Type')
    ref = fields.Char(string='Reference')
