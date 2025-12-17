FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "generate_resume.py"]
