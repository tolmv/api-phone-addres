FROM python:3.11-slim

WORKDIR /app

# ignore .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# don't buffer stdout and stderr
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 