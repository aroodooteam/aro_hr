# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class PaymentTerm(models.Model):

    _name = "payment.term"
    _description = "Mode de Reglement"

    def _get_default_rate(self, cr, uid, arg, context=None):
        terms = self.search(cr, uid,
                            [('employee_id', '=', context['employee_id'])],
                            context=None)
        terms = self.browse(cr, uid, terms, context=None)
        rate = 100
        for term in terms:
            rate = rate - term.rate
        return rate

    name = fields.Many2one(comodel_name='payment.mode', string='Mode De Reglement')
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee')
    bank_account_id = fields.Many2one(comodel_name='res.partner.bank', string='RIB')
    bank_id = fields.Many2one(comodel_name='res.bank', string='Bank', related='bank_account_id.bank', readonly=True)
    amount = fields.Float(string='Amount')
    rate = fields.Float(string='Rate')
    state = fields.Selection(selection=[('open', 'Actif'), ('cancel', 'Inactif')], string='State', default='open')
