FROM odoo:18

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    python3-venv

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip

COPY requirements.txt /tmp/
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]