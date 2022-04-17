from flask import Flask,render_template,request,make_response,redirect,url_for,flash
import uuid

app = Flask(__name__)

@app.route('/start')
def start():
    return "flask is running"

@app.route('/')
def hello_world():
    title = "Hello World"
    return render_template('index.html',title=title)

@app.route("/setcookie",methods=['POST','GET'])
def setcookie():

    fpid = request.cookies.get('fpid', None)
    if(fpid == None):

        ## generate a unique id
        fpid = str(uuid.uuid4())

    
    resp = make_response(render_template('index.html',title="FPIDをセットします",contents=fpid))
    resp.set_cookie('fpid',
        value=fpid,
        max_age=60*60*24*30*13,
        domain=request.host,
        path='/',
        secure=True,
        httponly=True,
        samesite='lax'
        )
    return resp

if __name__ == '__main__':
    app.run()