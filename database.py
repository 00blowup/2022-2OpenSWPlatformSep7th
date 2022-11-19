import pyrebase
import json 

class DBhandler:
    def __init__(self ):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f )
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    #RegisterPage
    def insert_restaurant(self,name,data,img_path):
        restaurant_info={
        "name":data['name'],
        "type":data['type'],
        "location":data['location'],
        "locatedetail":data['locationdetail'],
        "phone":data['phone'],
        "mon":{data['closed'],data['start'],data['end'],data['bstart'],data['bend']},
        "extra":data['extra'],
        "img_path":img_path
        }
        self.db.child("restaurant").child(name).set(restaurant_info)
        print(data,img_path)
        return True
