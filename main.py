from flask import Flask, render_template, jsonify # Flask의 결과를 JSON으로 준다

import requests
import json # python내에서 string to json 혹은 json to string

from pymongo import MongoClient  #pymongo 임포트하기
client = MongoClient(
    'mongodb://jin:jin47657306@ds011459.mlab.com:11459/heroku_xmp8k4vm?retryWrites=false',
    27017)
db = client['heroku_xmp8k4vm']

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/saveclicktrend', methods=['GET'])
def saveclicktrend():
    from flask import request as flask_request
    import os
    import sys
    import urllib.request

    client_id = "fPVMYT4OvJrl02aN6tjo"
    client_secret = "T4iTcJzO6Y"

    #input_body
    json_body = {
        "ages": [
          "20",
          "30"
        ],
        "category": [
          {
            "name": "디지털/가전",
            "param": [
              "50000003"
            ]
          },
          {
            "name": "화장품/미용",
            "param": [
              "50000002"
            ]
          }
        ],
        "device": "pc",
        "endDate": "2017-09-30",
        "gender": "f",
        "startDate": "2017-08-01",
        "timeUnit": "week"
      }
    
    if flask_request.args.get('startDate') is not None:
      json_body['startDate'] = flask_request.args.get('startDate')

    if flask_request.args.get('endDate') is not None:
      json_body['endDate'] = flask_request.args.get('endDate')

    if flask_request.args.get('timeUnit') is not None:
      json_body['timeUnit'] = flask_request.args.get('timeUnit')

    if flask_request.args.get('gender') is not None:
      json_body['gender'] = flask_request.args.get('gender')

    if flask_request.args.get('device') is not None:
      json_body['device'] = flask_request.args.get('device')

    if flask_request.data:
      request_body = flask_request.data.decode() # bytes to string
      request_body = json.loads(request_body) # string to JSON
      json_body['category'] = request_body['category']
      print(json_body)

    if flask_request.args.get('ages') is not None:
      json_body['ages'] = flask_request.args.get('ages').split(",")

    body = json.dumps(json_body) #JSON to string

    #ClickTrend
    url = "https://openapi.naver.com/v1/datalab/shopping/categories"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)
        response = response_json.copy()
        db.clicktrend.insert_one(response_json)
        return jsonify(response)
    else:
        print("Error Code:" + rescode)

    return jsonify(response_json)
    

@main.route('/savedeviceshare', methods=['GET'])
def savedeviceshare():
    from flask import request as flask_request
    import os
    import sys
    import urllib.request
    client_id = "fPVMYT4OvJrl02aN6tjo"
    client_secret = "T4iTcJzO6Y"

    #input_body
    json_body = {
  "startDate": "2017-08-01",
  "endDate": "2017-09-30",
  "timeUnit": "week",
  "category": "50000003",
  "gender": "f",
  "ages": [ "20",  "30"]
  }

    if flask_request.args.get('startDate') is not None:
      json_body['startDate'] = flask_request.args.get('startDate')

    if flask_request.args.get('endDate') is not None:
      json_body['endDate'] = flask_request.args.get('endDate')

    if flask_request.args.get('timeUnit') is not None:
      json_body['timeUnit'] = flask_request.args.get('timeUnit')

    if flask_request.args.get('category') is not None:
      json_body['category'] = flask_request.args.get('category')

    if flask_request.args.get('gender') is not None:
      json_body['gender'] = flask_request.args.get('gender')
    
    if flask_request.args.get('ages') is not None:
      json_body['ages'] = flask_request.args.get('ages').split(",")

    body = json.dumps(json_body)

    #deviceshare
    url = "https://openapi.naver.com/v1/datalab/shopping/category/device"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)
        response = response_json.copy()
        db.deviceshare.insert_one(response_json)
        return jsonify(response)
    else:
        print("Error Code:" + rescode)

@main.route('/savegendershare', methods=['GET'])
def savegendershare():
    from flask import request as flask_request
    import os
    import sys
    import urllib.request
    client_id = "fPVMYT4OvJrl02aN6tjo"
    client_secret = "T4iTcJzO6Y"

    #input_body
    json_body = {
  "startDate": "2017-08-01",
  "endDate": "2017-09-30",
  "timeUnit": "week",
  "category": "50000003",
  "device": "pc",
  "ages": [ "20",  "30"]
    } 

    if flask_request.args.get('startDate') is not None:
      json_body['startDate'] = flask_request.args.get('startDate')

    if flask_request.args.get('endDate') is not None:
      json_body['endDate'] = flask_request.args.get('endDate')

    if flask_request.args.get('timeUnit') is not None:
      json_body['timeUnit'] = flask_request.args.get('timeUnit')

    if flask_request.args.get('category') is not None:
      json_body['category'] = flask_request.args.get('category')

    if flask_request.args.get('gender') is not None:
      json_body['gender'] = flask_request.args.get('gender')
    
    if flask_request.args.get('ages') is not None:
      json_body['ages'] = flask_request.args.get('ages').split(",")

    body = json.dumps(json_body)

    #gendershare
    url = "https://openapi.naver.com/v1/datalab/shopping/category/gender"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)
        response = response_json.copy()
        db.gendershare.insert_one(response_json)
        return jsonify(response)
    else:
        print("Error Code:" + rescode)

@main.route('/clicktrend', methods=['GET'])
def clicktrend():
    pass


@main.route('/deviceshare', methods=['GET'])
def deviceshare():
    pass


@main.route('/gendershare', methods=['GET'])
def gendershare():
    pass


if __name__ == "__main__":
    main.run(host='0.0.0.0', port=8080)

    # # JSON to STRING
    # body = json.dumps(json_body)

    # # STRING to JSON
    # json_body = json.loads(body)
