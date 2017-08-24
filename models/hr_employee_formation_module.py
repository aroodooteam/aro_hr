# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrEmployeeFormationModule(models.Model):
    """Gestion des modules de formation chez ARO"""

    _name = 'hr.employee.formation.module'

 	code = fields.Char(string='Code',size=16)
 	name = fields.Char(string='Libellé',size=64)