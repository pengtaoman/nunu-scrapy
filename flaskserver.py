import waitress
from flask import Flask,render_template, stream_template
from flask import stream_with_context, request
from util import panflask
import json

app = Flask(__name__)

with app.app_context():
    dh = panflask.PanFlask()
    dh.load_movie_data()
    print('T'*200)

@app.route("/")
def hello_world():
    return "<p>"+dh.getdata()+"</p>"


@app.route('/querymovies', methods=['POST', 'GET'])
def querymovies():
    searchkey = request.form.get('searchkey')
    if searchkey == None:
        searchkey = request.args.get('searchkey') if request.args.get('searchkey') != None else ''
    name = searchkey
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
    queryreq['page'] = page
    queryreq['searchkey'] = searchkey
    queryjson = dh.search_movie(page, **query)

    lis = []

    for inx in range(40):
        try:
            js = next(queryjson)[1].to_json()
            row = json.loads(js)
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
    # print(slist)
    return render_template('movie.html', rows=slist, cas=dh.categories, couns=dh.countries, que=queryreq, hrf=hrf)



@app.route('/queryteleplays', methods=['POST', 'GET'])
def queryteleplays():
    searchkey = request.form.get('searchkey')
    if searchkey == None:
        searchkey = request.args.get('searchkey') if request.args.get('searchkey') != None else ''
    name = searchkey
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
    queryreq['page'] = page
    queryreq['searchkey'] = searchkey
    queryjson = dh.search_teleplay(page, **query)

    lis = []

    for inx in range(40):
        try:
            js = next(queryjson)[1].to_json()
            row = json.loads(js)
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
    # print(slist)
    return render_template('teleplay.html', rows=slist, cas=dh.categories, couns=dh.countries, que=queryreq, hrf=hrf)

if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=8088, threads=20)