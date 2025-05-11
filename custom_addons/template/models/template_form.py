import requests
from odoo import models, fields, api

class TemplateForm(models.Model):
    _name = 'template.form'
    _description = 'Forms by Template'

    name = fields.Char("Title")
    author = fields.Char("Author")
    question_ids = fields.One2many("template.form.question", "template_id", string="Questions")
