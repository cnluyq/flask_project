# flask_project
#### 使用说明

```
yum install python3        #install python

git clone git@gitee.com:cnluyq/flask_project.git
cd flask_project
python3 -m venv .env       #set up python virtual env
source .env/bin/activate   #activate python venv

pip3 install flask         #develop framework
pip3 install gunicorn      #wsgi server
pip3 install gevent        #cooperative multitasking python framework

gunicorn -c config.py main:app     #start gunicorn server

test: access to http://127.0.0.1:8081


######################
PS: if there is a nginx as proxy server in the front. you could choose to config nginx to let nginx transfer all requests to the gunicorn server. 
#####################
The way to config is 

$ which nginx                                  //to check if the nginx is installed.
/usr/local/webserver/nginx/sbin/nginx                  
$ nginx -t                                     //to find out where the nginx config is.
nginx: the configuration file /usr/local/webserver/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/local/webserver/nginx/conf/nginx.conf test is successful
$ vi /usr/local/webserver/nginx/conf/nginx.conf            //edit config file. add the following proxy_pass item to the gunicorn server/port
... ...
        location / {
            root   html;
            index  index.html index.htm;
            proxy_pass  http://127.0.0.1:8081;
        }
... ...

$ nginx -s reload              //reload nginx server to use the new config.

```
