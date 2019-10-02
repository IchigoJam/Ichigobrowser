from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def ichigo_proxy():
  url = request.args.get('u')
  return url

app.run(host = '0.0.0.0', port = 5001)
