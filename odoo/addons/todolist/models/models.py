# -*- coding: utf-8 -*-

from odoo import models, fields, api


class todolist(models.Model):
    _name = 'todolist.todolist'
    _description = 'To-do list'

    name = fields.Char()
    description = fields.Text()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
