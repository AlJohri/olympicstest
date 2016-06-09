# olympicstest

## Usage

**NOTE**: run separately. java is slow to start so keep it always running

1. Run the nlgserv in one tab.

```
docker-compose up --build nlgserv
```

2. Wait a few seconds until the nlgserv has started. Run the writer in another tab.

```
docker-compose build writer && docker-compose run writer
```