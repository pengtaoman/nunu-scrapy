import waitress
from flask import Flask,render_template, stream_template
from flask import stream_with_context, request
from util import json2mongo
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/querymovies', methods=['POST', 'GET'])
def querymovies():
    name = request.args.get('name') if request.args.get('name') != None else ''
    year = request.args.get('year') if request.args.get('year') != None else ''
    category = request.args.get('category') if request.args.get('category') != None else ''
    rate = request.args.get('rate') if request.args.get('rate') != None else ''
    actor = request.args.get('actor') if request.args.get('actor') != None else ''
    country = request.args.get('country') if request.args.get('country') != None else ''
    page = int(request.args.get('page')) if request.args.get('page') != None and int(request.args.get('page')) > 1 else 1
    query = {
        'name': name,
        'year': year,
        'country': country,
        'director': '',
        'category': category,
        'rate': rate,
        'actor': actor
        }
    queryreq = query.copy()

    searchkey = request.form.get('searchkey')
    if searchkey == None:
        searchkey = request.args.get('searchkey') if request.args.get('searchkey') != None else ''
    queryreq['page'] = page
    queryreq['searchkey'] = searchkey
    queryjson = json2mongo.queryjsonfilepage('./json/movie.json', (page - 1) * 40 + 1, page * 40,
                                             searchkey, **query)

    lis = []

    for inx in range(40):
        try:
            row = next(queryjson)
            # print(row['total'])
            img = str(row['link']).replace('dianying', 'img')
            img = img.replace('html', 'jpg')
            row['image'] = img
            lis.append(row)
        except StopIteration as e:
            break
    if len(lis) < 40:
        queryreq['nopage'] = 1
    else:
        queryreq['nopage'] = 0
    slist = sorted(lis, key=lambda d: d['rate'], reverse=True)
    hrf = {}
    hrf['catehrf'] = '?name='+name+'&&'+'year='+year+'&&'+'country='+country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['counhrf'] = '?name='+name+'&&'+'year='+year+'&&'+'category='+category+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['year'] = '?name=' + name + '&&' +'category=' + category+'&&'+'country='+country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['rate'] = '?name=' + name + '&&' + 'category=' + category + '&&' + 'country=' + country+'&&'+'searchkey='+searchkey
    hrf['actor'] = '?name=' + name + '&&' + 'category=' + category + '&&' + 'country=' + country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['page'] = '?name=' + name +'&&'+'year='+year+ '&&' + 'category=' + category + '&&' + 'country=' + country + '&&' + 'rate=' + rate+'&&'+'searchkey='+searchkey
    hrf['searchkey'] = '?name=' + name + '&&' + 'year=' + year + '&&' + 'category=' + category + '&&' + 'country=' + country + '&&' + 'rate=' + rate
    return render_template('movie.html', rows=slist, cas=json2mongo.categories, couns=json2mongo.countries, que=queryreq, hrf=hrf)

@app.route('/queryteleplays', methods=['POST', 'GET'])
def queryteleplays():
    name = request.args.get('name') if request.args.get('name') != None else ''
    year = request.args.get('year') if request.args.get('year') != None else ''
    category = request.args.get('category') if request.args.get('category') != None else ''
    rate = request.args.get('rate') if request.args.get('rate') != None else ''
    actor = request.args.get('actor') if request.args.get('actor') != None else ''
    country = request.args.get('country') if request.args.get('country') != None else ''
    page = int(request.args.get('page')) if request.args.get('page') != None and int(
        request.args.get('page')) > 1 else 1
    query = {
        'name': name,
        'year': year,
        'country': country,
        'director': '',
        'category': category,
        'rate': rate,
        'actor': actor
    }
    queryreq = query.copy()
    searchkey = request.form.get('searchkey')
    if searchkey == None:
        searchkey = request.args.get('searchkey') if request.args.get('searchkey') != None else ''
    queryreq['page'] = page
    queryreq['searchkey'] = searchkey
    queryjson = json2mongo.queryjsonfilepage('json/teleplay.json', (page - 1) * 40 + 1, page * 40,
                                             searchkey, **query)
    lis = []

    for inx in range(40):
        try:
            row = next(queryjson)
            # print(row['total'])
            img = str(row['link']).replace('dianshiju', 'img')
            img = img.replace('html', 'jpg')
            row['image'] = img
            lis.append(row)
        except StopIteration as e:
            break
    if len(lis) < 40:
        queryreq['nopage'] = 1
    else:
        queryreq['nopage'] = 0
    slist = sorted(lis, key=lambda d: d['rate'], reverse=True)
    hrf = {}
    hrf['catehrf'] = '?name='+name+'&&'+'year='+year+'&&'+'country='+country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['counhrf'] = '?name='+name+'&&'+'year='+year+'&&'+'category='+category+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['year'] = '?name=' + name + '&&' +'category=' + category+'&&'+'country='+country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['rate'] = '?name=' + name + '&&' + 'category=' + category + '&&' + 'country=' + country+'&&'+'searchkey='+searchkey
    hrf['actor'] = '?name=' + name + '&&' + 'category=' + category + '&&' + 'country=' + country+'&&'+'rate='+rate+'&&'+'searchkey='+searchkey
    hrf['page'] = '?name=' + name +'&&'+'year='+year+ '&&' + 'category=' + category + '&&' + 'country=' + country + '&&' + 'rate=' + rate+'&&'+'searchkey='+searchkey
    hrf['searchkey'] = '?name=' + name + '&&' + 'year=' + year + '&&' + 'category=' + category + '&&' + 'country=' + country + '&&' + 'rate=' + rate
    return render_template('teleplay.html', rows=slist, cas=json2mongo.categories, couns=json2mongo.countries,
                           que=queryreq, hrf=hrf)


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=8088, threads=20)