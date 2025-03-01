FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /django

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["ddtrace-run", "gunicorn", "sample_app.wsgi", "-c", "gunicorn.conf.py"]
