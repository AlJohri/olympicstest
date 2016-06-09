#!/bin/sh

touch log.stdout.txt log.stderr.txt
nlgserv 0.0.0.0 8000 log.stdout.txt log.stderr.txt &
tail -f log.stdout.txt log.stderr.txt