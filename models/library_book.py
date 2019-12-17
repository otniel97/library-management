# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book", default="New", required="True",)
    description = fields.Text(string="Description", required="True",)
    isbn = fields.Char(string="ISBN")

    #many to one
    #category_id = fields.Many2one(comodel_name="library.category", string="Categories", )

    # many to many
    #category_ids = fields.Many2many(comodel_name="library.category", string="Categories", )

    # one to many
    category_ids = fields.One2many(comodel_name="library.category", inverse_name="book_id",  string="Categories",)

    # campos calculados
    categ_count = fields.Integer(string="Number of categories", compute="_count_categ", )

    def _count_categ(self):
        for book in self:
            book.categ_count = len(book.category_ids)

    #constraints sql
    _sql_constraints = [('name_uniq', 'unique (name)', """Book name should be unique!"""),
                        #('isbn_uniq', 'unique (isbn)', """Book isbn should be unique!"""),
    ]

    #constraint python
    @api.constrains('isbn')
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError('ISBN duplicado')