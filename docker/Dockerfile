FROM python:3.7-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx
#    && apt-get -y install python3-dev \
#    && apt-get -y install build-essential
# COPY htdocs/ /var/www/html/
# RUN pip install -r requirements.txt --src /usr/local/src
# COPY docker/nginx.conf /etc/nginx/

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY docker/start.sh $APP_HOME

RUN chmod +x ./start.sh

CMD ["./start.sh"]
