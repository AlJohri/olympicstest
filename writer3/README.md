# writer3

## Usage

with bundler
```
bundle exec ruby app.rb
```

without bundler
```
jruby app.rb
```

with docker
```
docker-compose up --build writer3
```

## Setup

with bundler
```
rbenv install jruby-9.1.2.0
gem install bundler
bundle install
```

without bundler
```
gem install specific_install
gem specific_install https://github.com/jeremybmerrill/simplernlg.git
```
