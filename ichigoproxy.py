from flask import Flask, Response, request
import fetchkana

app = Flask(__name__)

@app.route('/')
def ichigo_proxy():
  url = request.args.get('u')
  t = fetchkana.fetchKana(url)
  return t.encode('CP932', 'ignore')

app.run(host = '0.0.0.0', port = 5001)
