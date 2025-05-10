FROM odoo:18

COPY requirements.txt /tmp/

RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

CMD ["odoo", "--config=/etc/odoo/odoo.conf"]