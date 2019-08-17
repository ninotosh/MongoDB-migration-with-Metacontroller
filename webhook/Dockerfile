FROM python:2.7-alpine

RUN pip install requests

COPY sync.py /srv

ENTRYPOINT ["python", "/srv/sync.py"]
