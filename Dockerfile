FROM python:3.8.19-slim-bullseye
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY *.py ./
COPY Procfile ./
CMD ["gunicorn",  "-b", "0.0.0.0:3000", "app:app"]
EXPOSE 5000
