import os
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

app = Flask(__name__)

def get_conn():
    response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
    content = response.read();
    content = content.split (':');
    response.close();
  
    return boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=content[0], aws_secret_access_key=content[1])
  

@app.route("/")
def index():
    return """
Available API endpoints:
"""

@app.route('/queues', methods=['GET'])
def get_queues(): 
    return Response(response="", mimetype="application/json")
  
@app.route('/queues', methods=['POST'])
def post_queues():
    return Response(response="", mimetype="application/json")

@app.route('/queues/<qid>', methods=['DELETE'])
def post_queues():
    return Response(response="", mimetype="application/json")

@app.route('/queues/<qid>/msgs', methods=['GET'])
def post_queues():
    return Response(response="", mimetype="application/json")

@app.route('/queues/<qid>/msgs/count', methods=['GET'])
def post_queues():
    return Response(response="", mimetype="application/json")

@app.route('/queues/<qid>/msgs', methods=['POST'])
def post_queues():
    return Response(response="", mimetype="application/json")

@app.route('/queues/<qid>/msgs', methods=['DELETE'])
def post_queues():
    return Response(response="", mimetype="application/json")


print get_conn()
