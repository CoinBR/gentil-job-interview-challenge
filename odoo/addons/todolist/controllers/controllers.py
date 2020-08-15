# -*- coding: utf-8 -*-
from odoo import http


# class Todolist(http.Controller):
#     @http.route('/todolist/todolist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todolist/todolist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todolist.listing', {
#             'root': '/todolist/todolist',
#             'objects': http.request.env['todolist.todolist'].search([]),
#         })

#     @http.route('/todolist/todolist/objects/<model("todolist.todolist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todolist.object', {
#             'object': obj
#         })
