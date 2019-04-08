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
    conn.commit()
    cur.close()
    conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
    else: 
        print("IDK")    
    return jsonify(response_object)
ITEMS=[]   
@app.route('/items', methods=['GET','POST'])
@cross_origin(origin='*')  
def items():
    response_object={'status': 'success'}
    if request.method=='GET':
        conn = db.get_db()
        sql="SELECT items.itemId, items.itemName, items.itemPortion, items.itemIngridents, items.itemNutrients, items.itemCalories, filters.filtername from filters inner join items on filters.filterid =  items.itemfilters"
        cur=conn.cursor()
        cur.execute(sql)
        items=cur.fetchall()
        it=[]
        for item in items:
            print(item)
            item={
                "itemId": item[0],
                "itemName": item[1],
                "itemPortion": item[2],
                "itemIngridents": item[3],
                "itemNutrients": item[4],
                "itemCalories": item[5],
                "itemFilters": item[6],
            }
            ITEMS.append(item)
            it.append(item)
        conn.commit()
        cur.close()
        conn.close()
        response_object.update({'items': it})
    elif request.method=='POST':
        post_data=request.get_json()
        itemId= post_data.get('itemId')
        itemName= post_data.get('itemName')
        itemPortion=post_data.get('itemPortion')
        itemIngridents=post_data.get('itemIngridents')
        itemCalories=post_data.get('itemCalories')
        itemNutrients= post_data.get('itemNutrients')
        itemFilters=post_data.get('filterId')       
        conn = db.get_db()
        '''insert into items ( itemid, itemname, itemPortion, itemIngridents, itemNutrients , itemfilters) values (%s, %s, %s, %s, %s,(select filterid from filters where filterid=%s));
insert into items ( itemid, itemname, itemfilters) values (4, 's', (select filterid from filters where filterid=1));
'''
        sql = "INSERT INTO items( itemId, itemName, itemPortion, itemIngridents, itemNutrients, itemCalories, itemFilters) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur=conn.cursor()
        val=(itemId, itemName, itemPortion, itemIngridents, itemNutrients, itemCalories, itemFilters)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(response_object)
@app.route('/calories', methods=['GET','POST'])
@cross_origin(origin='*')
def calCount(ITEMS):
    temp = ITEMS[0]
    for items in ITEMS:
            if (item) < (temp[calLoc]):
                temp = (ITEMS[x])
    return temp 
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
        conn.commit()
        cur.close()
        conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/periods', methods=['GET','POST'])
@cross_origin(origin='*')  
def periods():
    response_object={'status': 'success'}    
    pe=[]
    if request.method=='GET':
        conn = db.get_db()
        #sql = 'SELECT periodId, periodName,periodCategory FROM periods JOIN categories ON categories.categoryid = periods.periodcategory'
        sql = 'SELECT periodId, periodName FROM periods'
        cur=conn.cursor()
        cur.execute(sql)
        periods=cur.fetchall()
        for period in periods:
            period={
                'periodId':period[0], 
                'periodName': period[1]}
            pe.append(period)
        conn.commit()
        cur.close()
        conn.close()
        response_object.update({'periods': pe})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        periodId= post_data.get('periodId'),
        periodName=post_data.get('periodName')
        conn = db.get_db()
        sql = "INSERT INTO periods(periodId, periodName) VALUES (%s, %s)"
        cur=conn.cursor()
        val=(periodId, periodName)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()
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
        sql = 'SELECT preferenceId, preferenceCalories, preferenceNutrients FROM storedPreferences'
        cur=conn.cursor()
        cur.execute(sql)
        storedPreferences=cur.fetchall()
        for (key, val) in storedPreferences:
            print(key,val)
            #CAT.append({'preferenceId':key, 'preferenceCalories': val})
        conn.commit()
        cur.close()
        conn.close()
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
        conn.commit()
        cur.close()
        conn.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/user/<string:userEmail>', methods=['GET'])
@cross_origin(origin='*')  
def get_users(userEmail):
    response_object={}    
    conn = db.get_db()
    userEmail = request.args.get('userEmail')
    sql = "SELECT users.userName from users where users.useremail =userEmail"
    cur=conn.cursor()
    cur.execute(sql)
    users=cur.fetchone()
    print(users)
    conn.commit()
    cur.close()
    conn.close()
    user={
        "userName":users[0],        
    }
    response_object.update(user)
    return jsonify(response_object)
    
@app.route('/users', methods=['GET','POST'])
@cross_origin(origin='*')  
def users():
    response_object={}
    CAT=[]
    if request.method=='GET':
        conn = db.get_db()
        sql = 'SELECT userIdToken, userName , userLastName ,userEmail, isAdmin FROM users'
        cur=conn.cursor()
        cur.execute(sql)
        users=cur.fetchall()
        response_object.update({'users': users})
        conn.commit()
        cur.close()
        conn.close()
    elif request.method=='POST':
        post_data=request.get_json()
        tokenId= post_data.get('tokenId')
        firstName=post_data.get('firstName')
        lastName=post_data.get('lastName')
        email=post_data.get('email')
        if email == 'dorisgjata@gmail.com':
            isAdmin= True
        else:
            isAdmin=False
        response_object.update({'users': post_data}) 
        conn = db.get_db()    
       	sql = 'SELECT * FROM "addUser"(CAST(%s AS VARCHAR), CAST(%s AS TEXT), CAST(%s AS TEXT), CAST(%s AS TEXT), %s)'  
        # sql = " INSERT INTO users(userIdToken, userName , userLastName ,userEmail, isAdmin) VALUES (%s, %s, %s, %s, %s)"       
        cur=conn.cursor()
        val=(tokenId, firstName,lastName, email, isAdmin)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()
        print("done")
    return jsonify(response_object)

@app.route('/meal', methods=['GET','POST'])
@cross_origin(origin='*')  
def meal():
    response_object={'status': 'success'}    
    if request.method=='GET':
        conn = db.get_db()
        sql = "SELECT meal.mealId, meal.mealName, periods.periodname, a.itemName as itemname1, b.itemname as itemname2,  c.itemname as itemname3  from meal inner join items a on meal.foodItem1=a.itemid inner join items b on meal.foodItem2=b.itemid inner join items c on meal.foodItem3=c.itemid inner join periods on meal.mealperiod=periods.periodid;"
        cur=conn.cursor()
        cur.execute(sql)
        meals=cur.fetchall()
        me=[]
        for meal in meals:
            print(meal)
            meal={
                "mealId": meal[0],
                "mealName": meal[1],
                "mealPeriod": meal[2],
                "foodItem1": meal[3],
                "foodItem2": meal[4],
                "foodItem3": meal[5],
            }
            me.append(meal)
        conn.commit()
        cur.close()
        conn.close()
        response_object.update({'meals': me})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        mealId= post_data.get('mealId'),
        foodItem1=post_data.get('foodItem1')
        foodItem2=post_data.get('foodItem2')
        foodItem3=post_data.get('foodItem3')
        mealPeriod=post_data.get('mealPeriod')
        mealName=post_data.get('mealName')
        #response_object.update({'meal': FILT}) 
        conn = db.get_db()
        sql = "INSERT INTO meal( mealId, foodItem1, foodItem2, foodItem3, mealPeriod, mealName) VALUES (%s, %s, %s, %s, %s, %s)"
        cur=conn.cursor()
        val=(mealId, foodItem1,foodItem2, foodItem3, mealPeriod, mealName)
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()
    else: 
        print("IDK")    
    return jsonify(response_object)

@app.route('/user/<string:userEmail>/favourites', methods=['GET','POST'])
@cross_origin(origin='*')  
def favourites(userEmail):
    response_object={'status': 'success'}    
    FILT=[]
    if request.method=='GET':
        conn = db.get_db()
        userEmail = request.args.get('userEmail')
        sql = "SELECT favourites.favouriteItem, items.itemName from favourites INNER JOIN items on favourites.favouriteItem = items.itemid where favourites.useremail = userEmail"
       # sql = " SELECT coalesce( (select (favouriteMeal, favouriteItem) from favourites where favourites.useremail=''))"
        cur=conn.cursor()
        cur.execute(sql,(userEmail,))
        favs=cur.fetchall()
        favor=[]
        for fav in favs:
            fa={
                "favouriteItem": fav[0],
                "itemName": fav[1],
            }
            favor.append(fa)
        conn.commit()
        cur.close()
        conn.close()
        response_object.update({'favorites': favor})
    elif request.method=='POST':
        post_data=request.get_json()
        print(post_data)
        useremail= post_data.get('userEmail')
        favouriteItem=post_data.get('favouriteItem')
        favouriteMeal=post_data.get('favouriteMeal')
        favouriteRecommendation=post_data.get('favouriteRecommendation')
        conn = db.get_db()
        sql = "INSERT INTO favourites( useremail, favouriteItem, favouriteMeal,favouriteRecommendation) VALUES (%s, %s, %s, %s)"
        cur=conn.cursor()
        val=( useremail, favouriteItem, favouriteMeal,favouriteRecommendation )
        cur.execute(sql, val)
        conn.commit()
        cur.close()
        conn.close()
    else: 
        print("IDK")    
    return jsonify(response_object)
#DELETE AND UPDATE FUNCT
@app.route('/filters/<filterId>', methods=['GET','POST','DELETE'])
@cross_origin(origin='*')  
def single_filter(filterId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM filters WHERE filterId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(filterId)])
        conn.commit()
        cur.close()
        conn.close()
        response_object['message']="DELETED"
    elif request.method=='POST':
        post_data=request.get_json()
        filterID= post_data.get('filterId')
        filterNAME=post_data.get('filterName')
        conn = db.get_db()
        sql = 'UPDATE filters SET filterName = (%s) WHERE filters.filterId = (%s) '
        cur=conn.cursor()
        val=(filterNAME,filterID)
        cur.execute(sql,val)
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(response_object)

@app.route('/items/<itemId>', methods=['POST','DELETE'])
@cross_origin(origin='*')  
def single_item(itemId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM items WHERE itemId = (%s)'
        cur=conn.cursor()
        cur.execute(sql,(itemId))
        conn.commit()
        cur.close()
        conn.close()
    elif request.method=='POST':
        post_data=request.get_json()
        post_data=request.get_json()
        itemId= post_data.get('itemId')
        itemName= post_data.get('itemName')
        itemPortion= post_data.get('itemPortion')
        itemCalories= post_data.get('itemCalories')
        itemIngridents= post_data.get('itemIngridents')
        itemNutrients= post_data.get('itemNutrients')
        itemFilters= post_data.get('itemFilters')
        conn = db.get_db()
        #TODO: FULL UPDATE
        sql = 'UPDATE items SET itemName = (%s), itemPortion = (%s),  itemCalories = (%s), itemIngridents = (%s), itemNutrients = (%s) WHERE items.itemId = itemId'
        cur=conn.cursor()
        val=(itemName, itemPortion, itemCalories, itemIngridents, itemNutrients)
        cur.execute(sql,val)
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(response_object)

@app.route('/menu/<menuId>', methods=['POST','DELETE'])
@cross_origin(origin='*')  
def single_menu(menuId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM menu WHERE menuId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(menuId)])
        conn.commit()
        cur.close()
        conn.close()
    elif request.method=='POST':
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
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(response_object)

@app.route('/categorys/<categoryId>', methods=['GET','POST','DELETE'])
@cross_origin(origin='*')  
def single_category(categoryId):
    response_object={'status': 'success'}    
    if request.method=='DELETE':
        #post_data=request.get_json()
        conn = db.get_db()
        sql = 'DELETE FROM categorys WHERE categoryId = (%s)'
        cur=conn.cursor()
        cur.executemany(sql,[(categoryId)])
        conn.commit()
        cur.close()
        conn.close()
        response_object['message']="DELETED"
    elif request.method=='POST':
        post_data=request.get_json()
        categoryId= post_data.get('categoryId'),
        categoryName=post_data.get('categoryName')
        categoryItem=post_data.get('categoryItem')
        conn = db.get_db()
        sql = 'UPDATE categories SET categories.categoryName = (%s) WHERE categories.id = (%s) '
        cur=conn.cursor()
        cur.executemany(sql,[(categoryName, categoryId)])
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(response_object)
    
if __name__ == '__main__':
    app.run(debug=True)