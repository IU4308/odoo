from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import json
import requests

class ImportTemplateWizard(models.TransientModel):
    _name = 'template.import.wizard'
    _description = 'Import Templates from API'

    unified_token = fields.Char(string="API Token", required=True)

    def action_import(self):
        try:
            decoded = base64.b64decode(self.unified_token).decode()
            parsed = json.loads(decoded)
            api_url = parsed.get("api_url")
        except Exception as e:
            raise UserError(f"Invalid token format: {str(e)}")

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        grouped_by_template = {}
        for item in data:
            key = (item['template_title'], item['template_author'])
            grouped_by_template.setdefault(key, []).append(item)

        for (title, author), questions in grouped_by_template.items():
            template = self.env['template.form'].create({
                'name': title,
                'author': author
            })

            for q in questions:
                self.env['template.form.question'].create({
                    'template_id': template.id,
                    'question_text': q['question'],
                    'type': q['type'],
                    'aggregation': str(q.get('aggregation', '')),
                    'answers_count': q.get('answersCount', 0),
                })

        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }
