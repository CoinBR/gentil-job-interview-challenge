# -*- coding: utf-8 -*-

from odoo import models, fields, api

class todolist(models.Model):
    _name = 'todolist.todolist'
    _description = 'Task List'
    _rec_name = 'title'
    _order = 'title'

    title = fields.Char(size=50)
    description = fields.Text()
    status = fields.Selection([('01_created', 'Created'), ('02_working', 'Working'), ('03_done', 'Done'), ('99_problem', 'Problem')])
    partner = fields.Many2one(comodel_name='res.partner')
    due = fields.Datetime()
    color = fields.Integer(compute='_color')


    def _color(self):

        colorMap = { 
            '01_created': 0,
            '02_working': 3,
            '03_done': 10,
            '99_problem': 1,
            }

        for record in self:
            record.color = colorMap[record.status]

class ParentedPartner(models.Model):
    _inherit = 'res.partner'
    
    mother_name = fields.Char('Mother\'s full name')