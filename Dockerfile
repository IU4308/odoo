FROM odoo:18

USER root

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    python3-venv \
    libpq-dev \
    libsasl2-dev \
    python-dev \
    libssl-dev \
    libldap2-dev \
    build-essential

# Set up the virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip

COPY requirements.txt /tmp/

RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
ENV ADDONS_PATH="/mnt/addons,/mnt/custom_addons"

CMD ["odoo", "--config=/etc/odoo/odoo.conf"]
