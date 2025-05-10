FROM odoo:18

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    python3-venv

# Set up virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip

# Install the Python dependencies from requirements.txt
COPY requirements.txt /tmp/
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

# Set environment variables and run the Odoo container
ENV PATH="/opt/venv/bin:$PATH"
CMD ["odoo", "--config=/etc/odoo/odoo.conf"]