# -*- coding: utf-8 -*-

from odoo import models, fields, api

class todolist(models.Model):
    _name = 'todolist.todolist'
    _description = 'Task List'
    _rec_name = 'title'
    _order = 'title'

    title = fields.Char(size=50)
    description = fields.Text()
    status = fields.Selection([('created', 'Created'), ('working', 'Working'), ('done', 'Done'), ('problem', 'Problem')])
    due = fields.Datetime()