import requests
from odoo import api, SUPERUSER_ID

def import_templates_from_api(env, api_url, api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
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
        template = env['template.form'].create({
            'title': title,
            'author': author
        })

        for q in questions:
            env['template.form.question'].create({
                'template_id': template.id,
                'question_text': q['question'],
                'type': q['type'],
                'aggregation': str(q.get('aggregation', '')),
                'answers_count': q.get('answersCount', 0),
            })
