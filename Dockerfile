FROM python:3.10-slim
WORKDIR /app
COPY . .  # Ensure this copies ALL required files
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
