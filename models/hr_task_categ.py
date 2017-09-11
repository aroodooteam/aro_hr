# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _

class HrTaskCateg(models.Model):
    _name = 'hr.task.categ'
    _description = "Category"

    name = fields.Char (string = 'Category')