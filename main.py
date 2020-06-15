from flask import Flask, render_template, request, jsonify
from random import choice
import request
from bs4 import BeautifulSoup

from pymongo import MongoClient #pymongo 임포트하기
client = MongoClient('mongodb://jin:jin47657306@ds011459.mlab.com:11459/heroku_xmp8k4vm?retryWrites=false', 27017)
db = client['heroku_xmp8k4vm']

app = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/topten', methods=['GET'])
def displaytop10():
  #네이버쇼핑 검색 상위 10개 가져오기 (스크래핑)
  #썸네일, 텍스트, 가격
  #
  return jsonify({"result":[{"img":"a"},{"img":"b"}]})

@app.route('/clicktrend', methods=['GET'])
def clicktrend():
  pass

if __name__=="__main__":

  app.run(host='0.0.0.0', port=8080)