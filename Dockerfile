FROM python:3.7-alpine3.15
WORKDIR /alerter
COPY src .
CMD ["python3", "./main.py"]