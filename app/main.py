from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/",methods = ['POST', 'GET'])
def main():
	if request.method == 'POST':
		count = redis.incr('hits')
		return "thanks!"
	elif request.method == 'GET':
		count = redis.incr('hits',0)
		return str(count)
