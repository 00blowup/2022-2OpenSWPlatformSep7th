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
    def insert_restaurant(self,name,data,img_path):
        restaurant_info={
        "name":name,
        "type":data['type'],
        "location":data['location'],
        "locatedetail":data['locatedetail'],
        "phone":data['phone'],
        "monday":[data['start1'],data['end1'],data['bstart1'],data['bend1']],
        "tuesday":[data['start2'],data['end2'],data['bstart2'],data['bend2']],
        "wednesday":[data['start3'],data['end3'],data['bstart3'],data['bend3']],
        "thursday":[data['start4'],data['end4'],data['bstart4'],data['bend4']],
        "friday":[data['start5'],data['end5'],data['bstart5'],data['bend5']],
        "saturday":[data['start6'],data['end6'],data['bstart6'],data['bend6']],
        "sunday":[data['start7'],data['end7'],data['bstart7'],data['bend7']],
        "extra":data['extra'],
        "img_path":img_path
        }
        #restaurant_info = json.dumps(restaurant_info, default=str)
        #self.db.child("restaurant").child(name).set(restaurant_info)
        if self.restaurant_duplicate_check(name):
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
            if value['name'] == name:
                return False
        return True





    #AddMenu
    def insert_menu(self, data, img_path):
        #저장할 데이터 생성
        menu_info={
            "restaurant":data['restaurant'],
            "menuname":data['menuname'],
            "menuprice":data['menuprice'],
            "menudesc":data['menudesc'],
            "img_path":img_path
        }
        
        #중복체크
        if self.menu_duplicate_check(data['restaurant'], data['menuname']):
            self.db.child("menu").push(menu_info)
            print(data, img_path)
            return True
        else:      
            return False
    


    #메뉴 중복체크용 함수 (식당 이름과 메뉴 이름이 같으면 중복으로 판단)
    def menu_duplicate_check(self, restaurant, menuname):
        menus = self.db.child("menu").get()
        for menu in menus.each():
            value = menu.val()
            if value['restaurant']==restaurant and value['menuname']==menuname:
                return False
        return True
    
    
    
    
       
    #WriteReviewPage
    def insert_review(self,data,img_path):
        total_rating = ( (float(data['rating1']) + float(data['rating2']) + float(data['rating3']) + float(data['rating4']) + float(data['rating5']) + float(data['rating6'])) / 6.0 )
        total_rating = round(total_rating, 2)
        review_info = {
        "name":data['restaurant_name'],
        "rating1":int(data['rating1']),
        "rating2":int(data['rating2']),
        "rating3":int(data['rating3']),
        "rating4":int(data['rating4']),
        "rating5":int(data['rating5']),
        "rating6":int(data['rating6']),
        "total_rating":total_rating,
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
          self.db.child("account").child(ID).set(account_info)
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
        target_value = []
        for acc in accounts.each():
            value = acc.val()
            if value['UserId']==ID and value['UserPassword']==PW:
                return True
        return False
        
        

    #맛집 데이터 가져오기
    def get_restaurants(self):
        restaurants = self.db.child("restaurant").get().val()
        return restaurants

    
    #식당 이름을 기준으로 메뉴들 가져오기
    def get_menus_byResName(self, name):
        menus = self.db.child("menu").get()
        target_values = []
        for menu in menus.each():
            value = menu.val()
            if value['restaurant'] == name:
                target_values.append(value)
        return target_values
    
    
    
    # 맛집이름으로 restaurant 테이블에서 정보 가져오기  
    def get_restaurant_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                target_value = value
        return target_value
    
      # 맛집이름으로 review 테이블에서 평점 가져와 계산하기
    def get_avgrate_by_name(self, name):
        reviews = self.db.child("review").get()
        target_value = ""
        for res in reviews.each():
            value = res.val()
            if value['name'] == name:
                target_value = value['total_rating']
        return target_value

    
    #식당 이름을 기준으로 리뷰들 가져오기
    def get_reviews_byResName(self, name):
        reviews = self.db.child("review").get()
        target_values = []
        for review in reviews.each():
            value = review.val()
            if value['name'] == name:
                target_values.append(value)
        return target_values
    
    
    #특정 location에 해당하는 값 가져오기
    def get_restaurants_bylocation(self, cate):
        restaurants = self.db.child("restaurant").get()
        target_value=[]
        for res in restaurants.each():
            value=res.val()

            if value['location']== cate:
                target_value.append(value)
        print("######target_value",target_value)
        new_dict={}
        for k,v in enumerate(target_value):
            new_dict[k]=v
        return new_dict

    # 특정 type에 해당하는 값 가져오기
    def get_restaurants_bytype(self, cate):
        restaurants = self.db.child("restaurant").get()
        target_value=[]
        for res in restaurants.each():
            value=res.val()

            if value['type']== cate:
                target_value.append(value)
        print("######target_value",target_value)
        new_dict={}
        for k,v in enumerate(target_value):
            new_dict[k]=v
        return new_dict

    
