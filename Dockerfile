FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /django

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN pip3 install -r requirements.txt

RUN opentelemetry-bootstrap -a install

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "sample_app.wsgi"]
