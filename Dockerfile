# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN apt-get update
RUN apt-get -qq -y install curl

RUN apt-get install -y cron     # Install cron
COPY scripts/cron /etc/chron.d/cron
RUN chmod 0644 /etc/chron.d/cron #execution rights for chron job
RUN crontab /etc/chron.d/cron    # apply chron job
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log