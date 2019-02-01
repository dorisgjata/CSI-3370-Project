from flask import Flask, render_template
import os
import psycopg2
from . import db
app = Flask(__name__)
db.init_app(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/locations')
def locations():
    conn = db.get_db()
    sql = 'SELECT locationname FROM campuslocations'
    cur=conn.cursor()
    cur.execute(sql)
    locations=cur.fetchall()
    loc=[]
    for location in locations:
        loc.append(location[0])
    cur.close()
    return render_template('main.html', locations=loc)

if __name__ == '__main__':
    app.run(debug=True)