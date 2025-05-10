FROM odoo:18

USER root

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y wget gnupg \
    && echo "deb http://apt.postgresql.org/pub/repos/apt $(grep VERSION_CODENAME /etc/os-release | cut -d= -f2)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update && apt-get install -y \
    build-essential \
    libsasl2-dev \
    libssl-dev \
    libldap2-dev \
    python3-venv \
    libpq-dev

# Set up the virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip

COPY requirements.txt /tmp/

RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
ENV ADDONS_PATH="/mnt/addons,/mnt/custom_addons"

CMD ["odoo", "--config=/etc/odoo/odoo.conf"]
