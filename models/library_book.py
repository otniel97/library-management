# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBook(models.model):
    _name = "library.book"

    name = fields.Char(string="", required=False, )
    description = fields.Text(string="", required=False, )