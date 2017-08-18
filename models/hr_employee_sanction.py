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
# Generated by the OpenERP plugin for Dia !

# from osv import fields
from openerp.osv import fields, osv
import datetime


class hr_employee_sanction(osv.osv):
    """gestion des sanctions"""
    _name = 'hr.employee.sanction'
    _columns = {
        'motif': fields.char('Motif', size=64),
        'date': fields.date('Date'),
        'date_interview': fields.datetime('Date entretien'),
        'date_start': fields.date('Date debut sanction'),
        'date_end': fields.date('Date fin sanction'),
        'name': fields.many2one('hr.employee', 'Salarie'),
            'type':fields.many2one('sanction.type', 'Type de Sanction'),
        'description':fields.text('Commentaires'),
        'suite':fields.boolean('Avec suite'),
    }
hr_employee_sanction()