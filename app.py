from  flask import Flask,request,Response
from flask_cors import cross_origin
import json
from apps.regression import Regression

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
        data = {'datasetUrl':'https://storage.googleapis.com/kagglesdsdata/datasets/4979752/8375315/Thyroid_Diff.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240531%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240531T103411Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3de7e144731e720157a13116169504c4d3be1064dc4ae6a8cdbefb0cf41e0c4cf9fe4507924ae5387f16b37e43b7a652b525916a15cdc30ad42b5cbc278d025e096bcce60859ea88eb5b445f5e24babd1961fa95ea448972a64a574f96ec8bdfab626ffa8bd74f105321aef1a3260fcaf75e38467d61f8c7083541e94378f1ad12b687103f7656e17366c8eaeaf3407a65435bf198790ee285f607fa33158bc47d130e0c4fd61b5f2d3707b75758bed2f312d1b6db5ad205a1247330d188a06ba5706ab47598f4a88acd8b4d65e59420adf0cd0702df54c8d615b6b51ad4e06e85a1ffc4330038a64043ef399e9c8a4c028fd0c48df11d4c0833bfd34bcb37d9'}
        processed_data = Regression(data.get('datasetUrl')).run()
        resp =  json.dumps({'body':processed_data})
        print('resp',resp)
        return resp
    else:
        return 'hello regression from server'
    

@app.route('/test')
def test():
    data = {'datasetUrl':'https://storage.googleapis.com/kaggle-data-sets/2190/3685/compressed/bottle.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240531%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240531T090138Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5eb46aeaec12e7c91eacdb4aad8a40c2e1512467f05fcc5e3e6a1ce7dd45f70bf736fe2da598763977f51c8adb81eaa710445909e5388b57cd33d66d7a707ce39d49254e224a318165ce0770d256d7bc07ba27266bc2e3e03217ac95caaef88f9a8f50ef3f36c51c35a21cfea9f33c9f8a6da9b512c3231901da13b3d3623941a94e7f5ac64fb5c6f8b1ec473925e605af9d0d059c4c3f61fe7e1e33c27dfb65bf24b6718320e182d7a559dffcb00db9803348f7fae19aae1524188981599e9131b3af56bc8090e283f90265a0d460d3b9fd1e3d99081e0e905682194720092e3e5887d1917fa46a36965be92cdfbc42ffa43d7066d2849b703c61011cd47835'}
    processed_data = Regression(data.get('datasetUrl')).run()
    return 'ok'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)