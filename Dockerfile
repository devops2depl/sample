FROM python:3.11-slim

WORKDIR /app

COPY random_4_digits.py .

CMD ["python", "random_4_digits.py"]
