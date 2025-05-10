from odoo import models, fields, api
import json

class TemplateForm(models.Model):
    _name = 'template.form'
    _description = 'Simple Template Form'

    title = fields.Char("Title", required=True)
    author = fields.Char("Author")
    description = fields.Text("Description")