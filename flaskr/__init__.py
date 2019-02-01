from flask import Flask, render_template
import os
import psycopg2

from database import conn_close,conn_open
app = Flask(__name__)
conn = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")

@app.route('/')
def index():
    return 'Hello World'

@app.route('/locations')
def locations():
    sql = 'SELECT locationname FROM campuslocations'
    cur=conn.cursor()

    cur.execute(sql)
    locations=cur.fetchone()[0]
    loc=[]
    for location in locations:
        loc.append(location)

    conn.commit()

    cur.close()
    return render_template('main.html', location=locations)

if __name__ == '__main__':
    app.run(debug=True)