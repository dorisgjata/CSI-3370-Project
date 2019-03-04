from flask import Flask, render_template, jsonify,json
import os
from flask_cors import CORS
import psycopg2
from . import db
import json, requests, simplejson, urllib, datetime
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#db.init_app(app)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify('Hello')

@app.route('/locations')
def locations():
    conn = db.get_db()
    sql = 'SELECT locationname FROM campuslocations'
    cur=conn.cursor()
    cur.execute(sql)
    locations=cur.fetchall()
    array=[]
    for location in locations:
        array.append(location[0])
    cur.close()
    return jsonify(array)
    
@app.route('/filters')
def filters():
    conn = db.get_db()
    sql = 'SELECT filterName FROM filters'
    cur=conn.cursor()
    cur.execute(sql)
    filters=cur.fetchall()
    array=[]
    for filter in filters:
        array.append(filter[0])
    cur.close()
    return jsonify(array)

@app.route('/menu')
def menu():
    timestamp=str(datetime.datetime.today())
    print(timestamp)
    url="https://api.dineoncampus.com/v1/location/menu?site_id=5751fd3090975b60e048932a&platform=0&location_id=586fd0d93191a2088ec6388f&date="+timestamp
    data=requests.get(url) 
    response=data.json()    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)