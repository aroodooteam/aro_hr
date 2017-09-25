# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class HrEmployeeSanction(models.Model):
    """gestion des sanctions"""
    _name = 'hr.employee.sanction'
    _description = "Employee sanction"

    motif = fields.Char(string='Reason')
    date = fields.Date(string='Date')
    date_interview = fields.Datetime(string='Interview')
    date_start = fields.Date(string='Start')
    date_end = fields.Date(string='End')
    name = fields.Many2one(comodel_name='hr.employee', string='Employee')
    type = fields.Many2one(comodel_name='sanction.type', string='Sanction Type')
    description = fields.Text(string='Comments')
    suite = fields.Boolean(string='Avec suite')
