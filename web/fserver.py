from flask import Flask,render_template, stream_template
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


@app.route('/movies')
def hello(name=None):
    return render_template('movie.html', name=name)

@app.route('/querymovies', methods=['POST', 'GET'])
def querymovies():
    error = None
    # query = {
    #     'name': request.form['name'],
    #     'year': request.form['year'],
    #     'country': request.form['country'],
    #     'director': request.form['director'],
    #     'category': request.form['category'],
    #     'rate': request.form['rate'],
    #     'actor': request.form['actor']
    #     }
    query = {
        'name': '',
        'year': '',
        'country': '',
        'director': '',
        'category': request.args['category'],
        'rate': '6',
        'actor': ''
        }
    queryjson = json2mongo.queryjsonfile('/Users/pengtao/work/tmp/movie.json', **query)
    lis = []
    for inx in range(100):
        try:
            row = next(queryjson)
            img = str(row['link']).replace('dianying', 'img')
            img = img.replace('html', 'jpg')
            row['image'] = img
            lis.append(row)
        except StopIteration as e:
            break
    slist = sorted(lis, key=lambda d: d['rate'], reverse=True)
    return render_template('movie.html', rows=slist, cas=json2mongo.categories, couns=json2mongo.countries)

@app.route('/queryteleplays', methods=['POST', 'GET'])
def queryteleplays():
    error = None
    # query = {
    #     'name': request.form['name'],
    #     'year': request.form['year'],
    #     'country': request.form['country'],
    #     'director': request.form['director'],
    #     'category': request.form['category'],
    #     'rate': request.form['rate'],
    #     'actor': request.form['actor']
    #     }
    query = {
        'name': '',
        'year': '2022',
        'country': '中国大陆',
        'director': '',
        'category': '悬疑',
        'rate': '6',
        'actor': ''
        }
    queryjson = json2mongo.queryjsonfile('/Users/pengtao/work/tmp/teleplay.json', **query)
    lis = []
    for inx in range(50):
        try:
            row = next(queryjson)
            img = str(row['link']).replace('dianshiju', 'img')
            img = img.replace('html', 'jpg')
            row['image'] = img
            lis.append(row)
        except StopIteration as e:
            break
    return render_template('movie.html', rows=lis, cas=json2mongo.categorys)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8088)