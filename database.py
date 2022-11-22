import pyrebase
import datetime, json 
from flask import flash

class DBhandler:
    def __init__(self ):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f )
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

        
    #RegisterPage
    def insert_restaurant(self,data,img_path):
        restaurant_info={
        "name":data['name'],
        "type":data['type'],
        "location":data['location'],
        "locatedetail":data['locatedetail'],
        "phone":data['phone'],
        "monday":{data['start1'],data['end1'],data['bstart1'],data['bend1']},
        "tuesday":{data['start2'],data['end2'],data['bstart2'],data['bend2']},
        "wednesday":{data['start3'],data['end3'],data['bstart3'],data['bend3']},
        "thursday":{data['start4'],data['end4'],data['bstart4'],data['bend4']},
        "friday":{data['start5'],data['end5'],data['bstart5'],data['bend5']},
        "saturday":{data['start6'],data['end6'],data['bstart6'],data['bend6']},
        "sunday":{data['start7'],data['end7'],data['bstart7'],data['bend7']},
        "extra":data['extra'],
        "img_path":img_path
        }
        restaurant_info = json.dumps(restaurant_info, default=str)
        # self.db.child("restaurant").child(name).push(restaurant_info)
        if self.restaurant_duplicate_check(data['name']):
          self.db.child("restaurant").push(restaurant_info)
          print(data, img_path)
          return True
        else:
          return False



     # 식당이름 중복 체크 함수
     def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
           value = res.val()
           if value['name']==name:
                return False
        return true





    #AddMenu
    def insert_menu(self, data, img_path):
        #저장할 데이터 생성
        menu_info={
            "menuname":data['menuname'],
            "menuprice":data['menuprice'],
            "menudesc":data['menudesc'],
            "img_path":img_path
        }
        
        #중복체크
        if self.menu_duplicate_check(data['menuname']):
            return False
        else:      
            self.db.child("menu").push(menu_info)
            print(data, img_path)
            return True
    


    #메뉴 중복체크용 함수 (메뉴 이름이 같으면 중복으로 판단)
    def menu_duplicate_check(self, menuname):
        menus = self.db.child("menu").get()
        for menu in menus.each():
            value = menu.val()
            if value['menuname']==menuname:
                return False
        return True
    
    
    
    
       
    #WriteReviewPage
    def insert_review(self,data,img_path):
        review_info = {
        "rating1":data['rating1'],
        "rating2":data['rating2'],
        "rating3":data['rating3'],
        "rating4":data['rating4'],
        "rating5":data['rating5'],
        "rating6":data['rating6'],
        "review":data['review'],
        "img_path":img_path
        }

        self.db.child("review").push(review_info)
        print(data, img_path)
        return True
    
    
    
    # SignUp 계정 생성
    def insert_account(self, ID, data):
        #저장할 데이터 생성
        account_info={
            "UserId":data['UserId'],
            "UserPassword":data['UserPassword'],
        }
        # self.db.child("account").child(ID).push(account_info)
        if self.account_duplicate_check(ID):
          self.db.child("account").child(ID).push(account_info)
          print(data)
          return True
        else:
          return False

    
    # SignUp 계정 중복체크용 함수 (아이디가 등록되어 있으면 False)
    def account_duplicate_check(self, name):
        accounts = self.db.child("account").get()
        for acc in accounts.each():
            if acc.key()==name:
                return False
        return True
    
    
    # Login
    def user_login(self, ID, PW):
        accounts = self.db.child("account").get()
        for acc in accounts.each():
            if (acc.key() == ID) and (acc.val().get("UserPassword") == PW):
                flash("환영합니다")
                return True
        flash("회원정보가 일치하지 않습니다")
        return False
