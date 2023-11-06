import  os
from  gevent import monkey
monkey.patch_all()
import multiprocessing
debug = False
bind = "localhost:8081"           
pidfile = "gunicorn.pid"
accesslog="logs/gunicorn.log"
errorlog="logs/gunicorn.err.log"
workers = multiprocessing.cpu_count()*2 + 1
worker_class = "gevent"
daemon=True
