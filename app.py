from flask import Flask,render_template,request,make_response,redirect,url_for,flash,Markup
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


    ## if already set "fpid" cookie, then use cookie value
    fpid = request.cookies.get('fpid', None)

    fpid_query_param = request.args.get('fpid', None)

    if(fpid_query_param != None):
        fpid = fpid_query_param

    if(fpid == None):

        ## generate a unique id
        fpid = str(uuid.uuid4())

    contents = Markup("FPID: " + fpid + "<p>if use 'fpid' query param, then use query param value as FPID(override)</p>")
    
    resp = make_response(render_template('index.html',title="FPIDをセットします",contents=contents))
    resp.set_cookie('fpid',
        value=fpid,
        max_age=60*60*24*30*13,
        domain=request.host,
        path='/',
        secure=True,
        httponly=False,
        samesite='lax'
        )
    return resp

if __name__ == '__main__':
    app.run()