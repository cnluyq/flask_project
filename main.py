#main.py
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')  #for http://<hostname>:<port>/
def index():
    msg="这是首页!"
    return render_template("index.html",data=msg)  
    
@app.route('/news')  #for http://<hostname>:<port>/news
def newspage():
    newsContent="新闻"
    return render_template("news.html",data=newsContent)

if __name__ == '__main__':
    app.run()   #if use flask build-in sever, set up host/port like: app.run(port=2021,host='0.0.0.0')
