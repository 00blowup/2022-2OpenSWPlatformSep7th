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





    #메뉴 데이터 추가 함수
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
    
    #메뉴 데이터 삭제 함수
    def delete_menu (self, name):
        menus = self.db.child("menu").get()
        for menu in menus.each():
            value = menu.val()
            if value['menuname']==name:
                key = str(menu.key())
                self.db.child("menu").child(key).remove()
    
       
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
    
    
    def get_restaurant(self):
        restaurants = self.db.child("restaurant")
        return restaurants

    
    #식당 이름을 기준으로 메뉴들 가져오기
    def get_menus_byResName(self, name):
        menus = self.db.child("menu").get()
        target_values = []

        if self.db.child("menu").shallow().get().val():
            for menu in menus.each():
                if menu is None:
                    continue
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
        avg_rate = 0.0
        num = 0
        
        for res in reviews.each():
            value = res.val()
            if value['name'] == name:
                avg_rate += value['total_rating']
                num += 1
        
        if num > 0:
            avg_rate = avg_rate / num
                
        return avg_rate

    
    #식당 이름을 기준으로 식당 정보의 key 가져오기
    def get_resKey_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_key=""
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                target_key = res.key()
        return target_key
        
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

    
    #식당 수정을 위하여 요일별영업여부를 꺼내오는 함수
    def get_opening_days(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                target_value = value
        
        check = []

        if target_value["monday"][0] != " " and target_value["monday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["tuesday"][0] != " " and target_value["tuesday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["wednesday"][0] != " " and target_value["wednesday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["thursday"][0] != " " and target_value["thursday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["friday"][0] != " " and target_value["friday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["saturday"][0] != " " and target_value["saturday"][0] != "":
            check.append(True)
        else: check.append(False)

        if target_value["sunday"][0] != " " and target_value["sunday"][0] != "":
            check.append(True)
        else: check.append(False)
        
        return check
        

    #식당정보 수정 함수
    def edit_resinfo(self, key, data, img_path):

        #key에는 수정 대상인 식당의 Key 값이 담겨있음
        #해당 Key로 DB를 탐색하여, 그 데이터의 값들을 하나하나 update
        self.db.child("restaurant").child(key).update({"name": data.get("name")})
        self.db.child("restaurant").child(key).update({"type": data.get("type")})
        self.db.child("restaurant").child(key).update({"location": data.get("location")})
        self.db.child("restaurant").child(key).update({"locatedetail": data.get("locatedetail")})
        self.db.child("restaurant").child(key).update({"phone": data.get("phone")})
        self.db.child("restaurant").child(key).update({"monday": [data.get("start1"),data.get("end1"),data.get("bstart1"),data.get("bend1")]})
        self.db.child("restaurant").child(key).update({"tuesday": [data.get("start2"),data.get("end2"),data.get("bstart2"),data.get("bend2")]})
        self.db.child("restaurant").child(key).update({"wednesday": [data.get("start3"),data.get("end3"),data.get("bstart3"),data.get("bend3")]})
        self.db.child("restaurant").child(key).update({"thursday": [data.get("start4"),data.get("end4"),data.get("bstart4"),data.get("bend4")]})
        self.db.child("restaurant").child(key).update({"friday": [data.get("start5"),data.get("end5"),data.get("bstart5"),data.get("bend5")]})
        self.db.child("restaurant").child(key).update({"saturday": [data.get("start6"),data.get("end6"),data.get("bstart6"),data.get("bend6")]})
        self.db.child("restaurant").child(key).update({"sunday": [data.get("start7"),data.get("end7"),data.get("bstart7"),data.get("bend7")]})
        self.db.child("restaurant").child(key).update({"img_path": img_path})

        
        
    #식당의 기존 img_path를 얻어오는 함수
    def get_imgpath_byname(self, name):
        target_value= self.get_restaurant_byname(str(name))

        img_path = target_value["img_path"]
        
        return img_path
