from odoo import models, fields

class TemplateFormQuestion(models.Model):
    _name = 'template.form.question'
    _description = "Template's Question"

    template_id = fields.Many2one('template.form', string='Template', required=True, ondelete='cascade')
    question_text = fields.Text(string='Question', required=True)

    type = fields.Selection([
        ('single_line', 'Single Line'),
        ('multiple_line', 'Multiple Line'),
        ('integer_value', 'Integer Value'),
        ('checkbox', 'Checkbox'),
    ], string='Type', required=True)

    aggregation = fields.Char(string='Aggregated Result')
    answers_count = fields.Integer(string='Number of Answers', default=0)