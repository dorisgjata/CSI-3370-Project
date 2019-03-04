import json, requests, simplejson, urllib, datetime
from flask import json

def getLocationSchedules():
    timestamp=str(datetime.datetime.now())
    print(timestamp)
    url="https://api.dineoncampus.com/v1/events/upcoming_events?site_id=5751fd3090975b60e048932a&"+timestamp
    data=requests.get(url) 
    response=data.json()
    current_events=response['current_events']
    a={}
    for item in response:
        for events in current_events:
            a["title"]=events['title']
            a["description"]=events['description']
            a["endTime"]=events['end'][0:10]
            a["activeStatus"]=events['active']
    print(a)
    print(data.status_code)
    file = open("event"+timestamp+".txt", "x")
    return json.dump(response, file )
#getLocationSchedules()
def getLocationMenu():
    timestamp=str(datetime.datetime.today())
    print(timestamp)
    url="https://api.dineoncampus.com/v1/location/menu?site_id=5751fd3090975b60e048932a&platform=0&location_id=586fd0d93191a2088ec6388f&date="+timestamp
    data=requests.get(url) 
    response=data.json()
    menu=response["menu"]
    periods=menu["periods"]
    m={}
    c={}
    i={}
    n={}
    f={}
    for period in periods:
        m["name"]=period["name"]
        m["id"]=period["id"]
        print(m)
        categories=period["categories"]
        for category in categories:
            c["name"]=category["name"]
            c["id"]=category["id"]
            print(c)
            items=category["items"]
            for item in items:
                i["itemname"]=item["name"]
                i["itemid"]=item["id"]
                i["portion"]=item["portion"]
                i["ingredients"]=item["ingredients"]
                print(i)
                filters=item["filters"]
                nutrients=item["nutrients"]
                #TODO: separate nutrients and filters
                for filter in filters:
                    f["name"]=filter["name"]
                for nutrient in nutrients:
                    n["name"]=nutrient["name"]
                    n["value"]=nutrient["value"]    
    file = open("menu"+timestamp+".txt", "x")
    return response
    #json.dump(response, file ) 
#getLocationMenu()
