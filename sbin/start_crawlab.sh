#!/bin/sh
# __author__ = 'lish'

source ~/.bash_profile
source /etc/profile

if [ "$1"x = "worker"x ];then
    cd /data/server/crawlab/frontend && npm install
    nohup python /data/server/crawlab/crawlab/manage.py app >> /tmp/app.log 2>&1 &
    nohup python /data/server/crawlab/crawlab/bin/run_flower.py >> /tmp/flower.log 2>&1 &
    cd /data/server/crawlab/frontend
    nohup npm run serve >> /tmp/npm_serve.log 2>&1 &
fi
nohup python /data/server/crawlab/crawlab/bin/run_worker.py >> /tmp/worker.log 2>&1 &