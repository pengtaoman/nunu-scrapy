from flask import Flask
from waitress import serve
from flask import stream_with_context, request
from util import json2mongo
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/movie")
def query_movie():
    query = {
        'name': '',
        'year': '2022',
        'country': '中国大陆',
        'director': '',
        'category': '悬疑',
        'rate': '7',
        'actor': ''
        }

    queryjson = json2mongo.queryjsonfile('/Users/pengtao/work/tmp/teleplay.json', **query)
    lis = []

    for inx in range(50):
        try:
            row = next(queryjson)
            lis.append(row)
        except StopIteration as e:
            break


    # def generate():
    #     yield '['
    #     for row in queryjson:
    #         try:
    #             yield json.dumps(row) + ','
    #         except StopIteration as e:
    #             break
    #     yield ']'
    return app.response_class(json.dumps(lis), mimetype='application/json')
    # return app.response_class(generate(), mimetype='application/json')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8088)