FROM python:3.10

WORKDIR /app

# Install system packages including netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

# Entrypoint
ENTRYPOINT ["/wait-for-db.sh"]

# Default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
