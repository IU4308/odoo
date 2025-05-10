FROM odoo:18

USER root

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip

COPY requirements.txt /tmp/
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]