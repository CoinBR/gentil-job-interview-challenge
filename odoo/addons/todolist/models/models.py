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
    partner = fields.Many2one(comodel_name='res.partner')
    due = fields.Datetime()
    color = fields.Integer(compute='_color')


    def _color(self):

        colorMap = { 
            'created': 0,
            'working': 3,
            'done': 10,
            'problem': 1,
            }

        for record in self:
            record.color = colorMap[record.status]

class ParentedPartner(models.Model):
    _inherit = 'res.partner'
    
    mother_name = fields.Char('Mother\'s full name')