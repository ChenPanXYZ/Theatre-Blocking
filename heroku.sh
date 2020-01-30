#!/bin/sh
heroku create --app chenpangujingjing
heroku container:login
heroku container:push web --app chenpangujingjing
heroku container:release web --app chenpangujingjing
heroku open --app chenpangujingjing