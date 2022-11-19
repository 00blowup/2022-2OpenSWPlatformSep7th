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

        if self.restaurant_duplicate_check(name):
          self.db.child("restaurant").child(name).push(restaurant_info)
          print(data,img_path)
          return True
        else:
          return False



    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
          if res.key()==name:
            return False
        return True

    #AddMenu
    def insert_menu(self, data, img_path):
        #저장할 데이터 생성
        menu_info={
            "menuname":data['menuname'],
            "menuprice":data['menuprice'],
            "menudesc":data['menudesc'],
            "img_path":img_path
        }
      
        self.db.child("menu").push(menu_info)
        print(data, img_path)
        return True
    
    
    
      
    #WriteReviewPage
    def insert_review(self,name,data,img_path):
        review = {
        "rating1":data['rating1'],
        "rating2":data['rating2'],
        "rating3":data['rating3'],
        "rating4":data['rating4'],
        "rating5":data['rating5'],
        "rating6":data['rating6'],
        "review":data['review'],
        "img_path":img_path
        }

        self.db.child("review").child(name).set(review)
        print(data,img_path)
        return True


    #메뉴 중복체크용 함수 (식당 이름과 메뉴 이름이 모두 같으면 중복으로 판단)
    def menu_duplicate_check(self, restaurant, menuname):
        menus = self.db.child("menu").get()
        for menu in menus.each():
            if menu.restaurant()==restaurant and menu.menuname()==menuname:
                return False
        return True
