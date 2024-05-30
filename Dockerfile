FROM python:3.10-slim

WORKDIR /app

COPY . /app

COPY req.txt /app/LS

CMD ["python", "netscan.py"]
