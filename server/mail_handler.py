import pymongo
import json
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.Email_DB
def send_mail(data):
    collections=db.Mails
    collections.insert_one(data)
    return 
def view_inbox(username):
    inbox=[]
    collections=db.Mails
    cur=collections.find({"to":username})
    for i in cur:
        inbox.append(i)
    dict_inbox_json=json.dumps(inbox)
    return dict_inbox_json
    
def view_sent(username):
    sent=[]
    collections=db.Mails
    cur=collections.find({"from":username})
    for i in cur:
        del i["_id"]
        sent.append(i)

    sent = { "data" : sent }
    # print(sent)    
    dict_sent_json=json.dumps(sent)
    # # print("______")
    # print(dict_sent_json)
    return dict_sent_json 
          