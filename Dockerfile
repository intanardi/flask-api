FROM python:3.8-slim

COPY manage.py /flaskapp/manage.py
COPY /app/models.py /flaskapp/app/models.py

CMD ["python", "/flaskapp/manage.py"]