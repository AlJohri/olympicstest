FROM python:3.5-alpine
RUN apk add --no-cache git make perl openjdk7-jre
ADD ./nlgserv/requirements.txt /code/nlgserv/
RUN pip install --upgrade pip
RUN pip install -r /code/nlgserv/requirements.txt
ADD . /code
WORKDIR /code/nlgserv
EXPOSE 8000
CMD ["./start.sh"]
