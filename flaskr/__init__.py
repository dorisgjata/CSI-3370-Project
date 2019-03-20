from flask import Flask, render_template, jsonify,json, request
import os
from flask_cors import CORS, cross_origin
import psycopg2
from . import db
import json, requests, simplejson, urllib, datetime
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#db.init_app(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
def application(environ, start_response):
      if environ['REQUEST_METHOD'] == 'OPTIONS':
        start_response(
        '200 OK',
        [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
            ('Access-Control-Allow-Methods', 'POST'),
        ]
        )
        return ''

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

@app.route('/parsedmenu')
def parsedmenu():
    timestamp=str(datetime.datetime.today())
    print(timestamp)
    url="https://api.dineoncampus.com/v1/location/menu?site_id=5751fd3090975b60e048932a&platform=0&location_id=586fd0d93191a2088ec6388f&date="+timestamp
    data=requests.get(url) 
    response=data.json()    
    return jsonify(response)

@app.route('/filters', methods=['GET','POST'])
@cross_origin(origin='*')  
def filters():
    response_object={'status': 'success'}    
    FILT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT filterId, filterName FROM filters'
        cur=conn.cursor()
        cur.execute(sql)
        filters=cur.fetchall()
        for (key, val) in filters:
            FILT.append({'filterId':key, 'filterName': val})
        cur.close()
        response_object.update({'filters': FILT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        filterID= post_data.get('filterId'),
        filterNAME=post_data.get('filterName')
        print('here')
        FILT.append({'filterId':filterID, 'filterName': filterNAME})
        response_object.update({'filters': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO filters(filterId, filterName) VALUES (%s, %s)"
        cur=conn.cursor()
        val=(filterID,filterNAME)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)
    
@app.route('/items', methods=['GET','POST'])
@cross_origin(origin='*')  
def items():
    response_object={'status': 'success'}
    ITEM=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT itemId, itemName, itemPortion, itemingridents, itemNutrients FROM items JOIN filters ON filters.filterid = items.itemfilters'
        cur=conn.cursor()
        cur.execute(sql)
        items=cur.fetchall()
        for (key, val) in items:
            print(key, val)
        cur.close()
        response_object.update({'items': ITEM})
    elif request.method=='POST':
        post_data=request.get_json()
        itemId= post_data.get('itemId')
        itemName= post_data.get('itemName')
        itemPortion=post_data.get('itemPortion')
        itemIngredients=post_data.get('itemIngredients')
        itemNutrients= post_data.get('itemNutrients')
        itemFilters=post_data.get('itemFilters')       
        conn = db.get_db()
        sql = "INSERT INTO items( itemId, itemName, itemPortion, itemIngredients, itemNutrients , itemFilters) VALUES (%s, %s, %s, %s, %s, %s)"
        cur=conn.cursor()
        val=(itemId, itemName, itemPortion, itemIngredients, itemNutrients , itemFilters)
        cur.execute(sql, val)
        cur.close()
    return jsonify(response_object)

@app.route('/menu', methods=['GET','POST'])
@cross_origin(origin='*')  
def menu():
    response_object={'status': 'success'}
    MENU=[]
    if request.method=='GET':
        conn = db.get_db()
        #CHECK this 
        sql = 'SELECT menuId, menuDate, menuName, fromDate, toDate FROM menu JOIN campuslocations ON campuslocations.locationid = menu.locationID JOIN items ON items.itemid = menu.fooditem'
        cur=conn.cursor()
        cur.execute(sql)
        menus=cur.fetchall()
        for (key, val) in menus:
            print(key, val)
        cur.close()
        response_object.update({'menu': MENU})
    elif request.method=='POST':
        post_data=request.get_json()
        menuId= post_data.get('menuId')
        menuDatw= post_data.get('menuDate')
        menuName= post_data.get('menuName')
        fromDate=post_data.get('fromDate')
        menuIngredients=post_data.get('menuIngredients')
        toDate= post_data.get('toDate')
        locationId=post_data.get('locationID') 
        foodItem=post_data.get('foodItem')           
        conn = db.get_db()
        sql = "INSERT INTO menu( menuId, menuDate, menuName, fromDate, menuIngredients, toDate , locationID,foodItem) VALUES (%s, %s, %s, %s, %s, %s,%s, %s)"
        cur=conn.cursor()
        val=(menuId, menuName, fromDate, menuIngredients, toDate , locationId)
        cur.execute(sql, val)
        cur.close()
    return jsonify(response_object)

@app.route('/categories', methods=['GET','POST'])
@cross_origin(origin='*')  
def categories():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT categoryId, categoryName, categoryItems FROM categories JOIN items ON items.itemid=categories.categoryid'
        cur=conn.cursor()
        cur.execute(sql)
        categorys=cur.fetchall()
        for (key, val) in categorys:
            print(key,val)
            #CAT.append({'categoryId':key, 'categoryName': val})
        cur.close()
        response_object.update({'categories': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        categoryId= post_data.get('categoryId'),
        categoryName=post_data.get('categoryName')
        categoryItem=post_data.get('categoryItem')
        print('here')
        #FILT.append({'categoryId':categoryID, 'categoryName': categoryNAME})
        response_object.update({'categorys': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO categorys(categoryId, categoryName, categoryItem) VALUES (%s, %s, %s)"
        cur=conn.cursor()
        val=(categoryId, categoryName, categoryItem)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/periods', methods=['GET','POST'])
@cross_origin(origin='*')  
def periods():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT periodId, periodName, periodCategory FROM periods JOIN categories ON categories.categoryid = periods.periodcategory'
        cur=conn.cursor()
        cur.execute(sql)
        periods=cur.fetchall()
        for (key, val) in periods:
            print(key,val)
            #CAT.append({'periodId':key, 'periodName': val})
        cur.close()
        response_object.update({'periods': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        periodId= post_data.get('periodId'),
        periodName=post_data.get('periodName')
        periodCategory=post_data.get('periodCategory')
        #FILT.append({'periodId':periodID, 'periodName': periodNAME})
        response_object.update({'periods': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO periods(periodId, periodName,periodCategory) VALUES (%s, %s, %s)"
        cur=conn.cursor()
        val=(periodId, periodName, periodCategory)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/storedPreferences', methods=['GET','POST'])
@cross_origin(origin='*')  
def storedPreferences():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT preferenceId, preferenceCalories, preferenceNutrients FROM storedPreferences JOIN categories ON categories.categoryid = storedPreferences.periodcategory'
        cur=conn.cursor()
        cur.execute(sql)
        storedPreferences=cur.fetchall()
        for (key, val) in storedPreferences:
            print(key,val)
            #CAT.append({'preferenceId':key, 'preferenceCalories': val})
        cur.close()
        response_object.update({'storedPreferences': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        preferenceId= post_data.get('preferenceId'),
        preferenceCalories=post_data.get('preferenceCalories')
        preferenceNutrients=post_data.get('preferenceNutrients')
        #FILT.append({'preferenceId':periodID, 'preferenceCalories': periodNAME})
        response_object.update({'storedPreferences': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO storedPreferences(preferenceId, preferenceCalories,preferenceNutrients) VALUES (%s, %s, %s)"
        cur=conn.cursor()
        val=(preferenceId, preferenceCalories, preferenceNutrients)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/users', methods=['GET','POST'])
@cross_origin(origin='*')  
def users():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT userId, userName, userPassword FROM users JOIN categories ON categories.categoryid = users.periodcategory'
        cur=conn.cursor()
        cur.execute(sql)
        users=cur.fetchall()
        for (key, val) in users:
            print(key,val)
            #CAT.append({'userId':key, 'userName': val})
        cur.close()
        response_object.update({'users': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        userId= post_data.get('userId'),
        userName=post_data.get('userName')
        userPassword=post_data.get('userPassword')
        #FILT.append({'userId':periodID, 'userName': periodNAME})
        response_object.update({'users': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO users(userId, userName,userPassword) VALUES (%s, %s, %s)"
        cur=conn.cursor()
        val=(userId, userName, userPassword)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/meal', methods=['GET','POST'])
@cross_origin(origin='*')  
def meal():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT mealId, foodItem1, foodItem2, foodItem3, mealPeriod FROM meal'
        cur=conn.cursor()
        cur.execute(sql)
        meal=cur.fetchall()
        for (key, val) in meal:
            print(key,val)
            #CAT.append({'mealId':key, 'mealCalories': val})
        cur.close()
        response_object.update({'meal': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        mealId= post_data.get('mealId'),
        foodItem1=post_data.get('foodItem1')
        foodItem2=post_data.get('foodItem2')
        foodItem3=post_data.get('foodItem3')
        mealPeriod=post_data.get('mealPeriod')
        #FILT.append({'mealId':periodID, 'mealCalories': periodNAME})
        response_object.update({'meal': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO meal( mealId, foodItem1, foodItem2, foodItem3, mealPeriod) VALUES (%s, %s, %s, %s, %s)"
        cur=conn.cursor()
        val=(mealId, mealCalories, mealNutrients)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/favourites', methods=['GET','POST'])
@cross_origin(origin='*')  
def meal():
    response_object={'status': 'success'}    
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT mealId, foodItem1, foodItem2, foodItem3, mealPeriod FROM meal'
        cur=conn.cursor()
        cur.execute(sql)
        meal=cur.fetchall()
        for (key, val) in meal:
            print(key,val)
            #CAT.append({'mealId':key, 'mealCalories': val})
        cur.close()
        response_object.update({'meal': CAT})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        mealId= post_data.get('mealId'),
        foodItem1=post_data.get('foodItem1')
        foodItem2=post_data.get('foodItem2')
        foodItem3=post_data.get('foodItem3')
        mealPeriod=post_data.get('mealPeriod')
        #FILT.append({'mealId':periodID, 'mealCalories': periodNAME})
        response_object.update({'meal': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO meal( mealId, foodItem1, foodItem2, foodItem3, mealPeriod) VALUES (%s, %s, %s, %s, %s)"
        cur=conn.cursor()
        val=(mealId, mealCalories, mealNutrients)
        cur.execute(sql, val)
        cur.close()
    else: 
        print("IDK")    
    return jsonify(response_object)
#DELETE AND UPDATE FUNCT
@app.route('/filters/<filterId>', methods=['GET','PUT','DELETE'])
@cross_origin(origin='*')  
def single_filter(filterId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM filters WHERE filterId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(filterId)])
        cur.close()
        response_object['message']="DELETED"
    elif request.method=='PUT':
        post_data=request.get_json()
        filterID= post_data.get('filterId')
        filterNAME=post_data.get('filterName')
        conn = db.get_db()
        sql = 'UPDATE filters SET filters.filterName = (%s) WHERE filters.id = (%s) '
        cur=conn.cursor()
        cur.executemany(sql,[(filterNAME,filterID)])
        cur.close()
    return jsonify(response_object)

@app.route('/items/<itemId>', methods=['PUT','DELETE'])
@cross_origin(origin='*')  
def single_item(itemId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM items WHERE itemId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(itemId)])
        cur.close()
    elif request.method=='PUT':
        post_data=request.get_json()
        post_data=request.get_json()
        itemId= post_data.get('itemId')
        itemName= post_data.get('itemName')
        itemPortion= post_data.get('itemPortion')
        itemIngredients= post_data.get('itemIngredients')
        itemNutrients= post_data.get('itemNutrients')
        itemFilters= post_data.get('itemFilters')
        conn = db.get_db()
        #TODO: FULL UPDATE
        sql = 'UPDATE items SET items.itemName = (%s) WHERE item.itemId = (%s) '
        cur=conn.cursor()
        cur.executemany(sql,[(filterNAME,itemId)])
        cur.close()
    return jsonify(response_object)

@app.route('/menu/<menuId>', methods=['PUT','DELETE'])
@cross_origin(origin='*')  
def single_menu(menuId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM menu WHERE menuId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(menuId)])
        cur.close()
    elif request.method=='PUT':
        post_data=request.get_json()
        menuId= post_data.get('menuId')
        menuDatw= post_data.get('menuDate')
        menuName= post_data.get('menuName')
        fromDate=post_data.get('fromDate')
        menuIngredients=post_data.get('menuIngredients')
        toDate= post_data.get('toDate')
        locationId=post_data.get('locationId') 
        foodItem=post_data.get('foodItem')           
        conn = db.get_db()
        conn = db.get_db()
        #TODO: FULL UPDATE
        sql = 'UPDATE menu SET menus.menuName = (%s) WHERE menu.menuId = (%s) '
        cur=conn.cursor()
        cur.executemany(sql,[(filterNAME,menuId)])
        cur.close()
    return jsonify(response_object)

@app.route('/categorys/<categoryId>', methods=['GET','PUT','DELETE'])
@cross_origin(origin='*')  
def single_category(categoryId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM categorys WHERE categoryId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(categoryId)])
        cur.close()
        response_object['message']="DELETED"
    elif request.method=='PUT':
        post_data=request.get_json()
        categoryId= post_data.get('categoryId'),
        categoryName=post_data.get('categoryName')
        categoryItem=post_data.get('categoryItem')
        conn = db.get_db()
        sql = 'UPDATE categories SET categories.categoryName = (%s) WHERE categories.id = (%s) '
        cur=conn.cursor()
        cur.executemany(sql,[(categoryName, categoryId)])
        cur.close()
    return jsonify(response_object)
    
if __name__ == '__main__':
    app.run(debug=True)