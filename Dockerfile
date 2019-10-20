FROM python:3.7-alpine

RUN pip install bottle gunicorn

COPY libkinkaid /app/libkinkaid/
COPY www/web.py /app

WORKDIR /app
CMD ["gunicorn", "-b 0.0.0.0:8000", "--workers=2", "--threads=5", "--access-logfile=-", "web"]
