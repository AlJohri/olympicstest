FROM python:3.5-alpine
RUN apk add --no-cache git make perl
ADD ./writer/requirements.txt /code/writer/
RUN pip install --upgrade pip
RUN pip install -r /code/writer/requirements.txt
ADD . /code
WORKDIR /code/writer
EXPOSE 5000
CMD ["./start.sh"]
