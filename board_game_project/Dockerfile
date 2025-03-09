FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]


docker build -t your-image-name .


RUN the Docker Container:**

Docker run -it --rm your-image-name