# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/library-management(http.Controller):
#     @http.route('/extra-addons/library-management/extra-addons/library-management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/library-management/extra-addons/library-management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/library-management.listing', {
#             'root': '/extra-addons/library-management/extra-addons/library-management',
#             'objects': http.request.env['extra-addons/library-management.extra-addons/library-management'].search([]),
#         })

#     @http.route('/extra-addons/library-management/extra-addons/library-management/objects/<model("extra-addons/library-management.extra-addons/library-management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/library-management.object', {
#             'object': obj
#         })