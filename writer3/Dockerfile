FROM jruby:9.1.2.0-jre
RUN apt-get update
RUN apt-get install -y git
ADD . /code
WORKDIR /code/writer3
RUN bundle install
CMD ["bundle", "exec", "ruby", "/code/writer3/app.rb"]