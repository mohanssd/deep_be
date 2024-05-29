from  flask import Flask,request,Response
from flask_cors import cross_origin
import json

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'

@app.route('/regression',methods = ['GET','POST','OPTIONS'])
@cross_origin()
def regression():
    print('-=-================action triggrered',request.origin)
    if request.method =="POST" or "OPTIONS":
        data = json.loads(request.data)
        # print('=======headers',request.headers)
        print('data from front end',data)
  
        resp =  Response(data)
        print('resp',resp)
        return json.dumps(data)
    else:
        return 'hello regression from server'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)