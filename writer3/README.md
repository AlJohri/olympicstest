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
brew update && brew upgrade rbenv ruby-build
rbenv install $(cat .ruby-version)
gem install bundler
bundle install
```

without bundler
```
gem install specific_install
gem specific_install https://github.com/jeremybmerrill/simplernlg.git
```
