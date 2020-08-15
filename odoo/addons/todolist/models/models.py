# -*- coding: utf-8 -*-

from odoo import models, fields, api

class task(models.Model):
    _name = 'todolist.task'
    _description = 'Lista de Tarefas'
    _rec_name = 'title'
    _order = 'title'

    title = fields.Char(size=50)
    description = fields.Text()
    done = fields.Boolean(default=False)
    created = fields.create_date()
    due = fields.Datetime()