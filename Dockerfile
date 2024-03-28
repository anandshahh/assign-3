#Acquiring Python 3.13
FROM python:3.13.0a5-slim-bookworm

#Make app folder on root
RUN mkdir -p /app

#Set working directory for application
WORKDIR /app

#Copy installation direction file and perform packages installation
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#Copy application to working directoy
COPY *.py ./
COPY Procfile ./

#Run app with gunicorn 
CMD ["gunicorn",  "-b", "0.0.0.0:5000", "app:app"]

EXPOSE 5000
