#!/bin/sh
heroku login
heroku create --app chenpangujingjing
heroku container:login
heroku container:push web --app chenpangujingjing
heroku container:release web --app chenpangujingjings
heroku open --app chenpangujingjing