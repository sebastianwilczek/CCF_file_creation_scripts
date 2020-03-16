#!/bin/bash

while true
do
	randomString=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 5 ; echo '')
	wget -e robots=off -H --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -r -l 1 -nd -A pdf http://scholar.google.com/scholar?q=filetype%3Apdf+($randomString)&btnG=&hl=en&as_sdt=0%2C23 -o /dev/null
done
