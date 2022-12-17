from flask import Flask, render_template, request, flash, redirect, url_for, session
import math
import numpy as np
from database import DBhandler
import hashlib
import sys

application = Flask(__name__)
application.secret_key = 'eatwha_secret'

DB = DBhandler()

@application.route("/")
def index():
    #return render_template("index.html")
    return redirect(url_for("index_restaurants"))

@application.route("/addmenu")
def addmenu():
    return render_template("AddMenu.html")

@application.route("/bytypepage")
def bytypepage():
    return render_template("ByTypePage.html")

@application.route("/ganadapage")
def ganadapage():
    return  redirect(url_for('ganadalist_restaurants'))

import json

@application.route("/ganadalist")
def ganadalist_restaurants():
    import numpy as np

    data = DB.get_restaurant().get()

    res=list()
    for datas in data.each():
        res.append(datas.val())

    name=list()
    i=0
    for rest in res:
        name.append(res[i]['name'])
        i+=1
    print(name)

    name.sort()
    
    ga_name=list(); na_name=list(); da_name=list() ;ra_name=list()
    ma_name=list(); ba_name=list(); sa_name=list(); aa_name=list()
    ja_name=list(); cha_name=list(); ka_name=list(); ta_name=list()
    fa_name=list(); ha_name=list()

    x=0
    for res in name:
        if (name[x][0]) <'나':
            ga_name.append(name[x])
        elif('나'<=(name[x][0]) and (name[x][0])<'다'):
            na_name.append(name[x])
        elif('다'<=(name[x][0]) and (name[x][0])<'라'):
            da_name.append(name[x])
        elif('라'<=(name[x][0]) and (name[x][0])<'마'):
            ra_name.append(name[x])
        elif('마'<=(name[x][0]) and (name[x][0])<'바'):
            ma_name.append(name[x])
        elif('바'<=(name[x][0]) and (name[x][0])<'사'):
            ba_name.append(name[x])
        elif('사'<=(name[x][0]) and (name[x][0])<'아'):
            sa_name.append(name[x])
        elif('아'<=(name[x][0]) and (name[x][0])<'자'):
            aa_name.append(name[x])
        elif('자'<=(name[x][0]) and (name[x][0])<'차'):
            ja_name.append(name[x])
        elif('차'<=(name[x][0]) and (name[x][0])<'카'):
            cha_name.append(name[x])
        elif('카'<=(name[x][0]) and (name[x][0])<'타'):
            ka_name.append(name[x])
        elif('타'<=(name[x][0]) and (name[x][0])<'파'):
            ta_name.append(name[x])
        elif('파'<=(name[x][0]) and (name[x][0])<'하'):
            fa_name.append(name[x])
        else:
            ha_name.append(name[x])
        x+=1
    
    return render_template("GanadaPage.html", ga_data=json.dumps(ga_name, ensure_ascii=False), na_data=json.dumps(na_name, ensure_ascii=False), da_data=json.dumps(da_name, ensure_ascii=False), 
    ra_data=json.dumps(ra_name, ensure_ascii=False), ma_data=json.dumps(ma_name, ensure_ascii=False), ba_data=json.dumps(ba_name, ensure_ascii=False), sa_data=json.dumps(sa_name, ensure_ascii=False), 
    aa_data=json.dumps(aa_name, ensure_ascii=False), ja_data=json.dumps(ja_name, ensure_ascii=False), cha_data=json.dumps(cha_name, ensure_ascii=False), ka_data=json.dumps(ka_name, ensure_ascii=False), 
    ta_data=json.dumps(ta_name, ensure_ascii=False), fa_data=json.dumps(fa_name, ensure_ascii=False), ha_data=json.dumps(ha_name, ensure_ascii=False))

#리스트 페이징
@application.route("/restaurant_list")
def list_restaurants():
    page = request.args.get("page",0,type=int)
    category = request.args.get("category","all")
    limit=5
    start_idx=limit*page
    end_idx=limit*(page+1)

    if category == "all":
        data=DB.get_restaurants()
    elif category == "locate-inschool" or category =="locate-frontdoor" or category=="locate-backdoor":
        data=DB.get_restaurants_bylocation(category)
    else:
        data=DB.get_restaurants_bytype(category)

    tot_count=len(data)
    print("category",category,tot_count)
    if tot_count<=limit:
        data=dict(list(data.items())[:tot_count])
    else:
        data=dict(list(data.items())[start_idx:end_idx])
    data= dict(sorted(data.items(),key=lambda x:x[1]['name'],reverse=False))
    return render_template(
        "RestaurantList.html",
        datas=data.items(),
        total=tot_count,
        limit=limit,
        page=page,
        page_count=math.ceil(tot_count/10),
        category=category
        )

@application.route("/locationtypepage")
def locationtypepage():
    return render_template("LocationTypePage.html")

@application.route("/login")
def login():
    return render_template("Login.html")


@application.route("/signup")
def signup():
    return render_template("SignUp.html")

@application.route("/registerpage")
def registerpage():
    return render_template("RegisterPage.html")


@application.route("/specificscreen")
def specificscreen():
    return render_template("SpecificScreen.html")

@application.route("/typespage")
def typespage():
    return render_template("TypesPage.html")

# 식당정보 수정 페이지 동적 라우팅
@application.route("/editres/<name>")
def editres(name):
    data = DB.get_restaurant_byname(str(name))
    check = DB.get_opening_days(str(name))
    for c in check:
        print(c)
    return render_template("EditRestaurant.html", data=data, check=check)

# 식당정보 수정 POST
@application.route("/editres", methods=['POST'])
def editpost():
    image_file=request.files["register_img"]
    newinfo = request.form

    if image_file:
        image_file.save("static/upload/{}".format(image_file.filename))
        img_path="/static/upload/"+image_file.filename
        print("새 이미지가 등록됨 " + img_path)
    else:
        img_path=DB.get_imgpath_byname(str(newinfo.get("originalname")))
        print("새 이미지가 등록되지 않아 기존 이미지가 유지됨")
    
    key = DB.get_resKey_byname(str(newinfo.get("originalname")))

    DB.edit_resinfo(key, newinfo, img_path)
    
    data = DB.get_restaurant_byname(str(newinfo.get("name")))
    avg_rate = DB.get_avgrate_by_name(str(newinfo.get("name")))
    check = DB.get_opening_days(str(newinfo.get("name")))
    print("####data:",data)
    return render_template("SpecificScreen.html", data=data, avg_rate=avg_rate, check=check)

    

# 메뉴 페이지 동적 라우팅
@application.route("/viewmenu/<name>/")
def viewmenu(name):
    menus = DB.get_menus_byResName(str(name))   # 데이터 찾아오기
    
    num=len(menus)

    return render_template("ViewMenu.html", name=name, menus=menus, num=num)

@application.route("/viewreview")
def viewreview():
    return render_template("ViewReview.html")

@application.route("/writereview")
def writereview():
    return render_template("WriteReview.html")

@application.route("/mypage")
def mypage():
    return render_template("MyPage.html")


#찜한 식당 수정 POST	
@application.route("/submit_like", methods=['POST'])	
def req_like_submit():	
    if request.method == 'POST':	
        data = request.form	
        key = data.get("userId")	
        print(key, data.get("restaurant_name"), data.get("like"))	
        if DB.insert_like_restaurant(key, data):	
            return render_template("SpecificScreen.html", key=key, data=data)



#WriteReview
@application.route("/submit_review", methods=['POST'])
def reg_review_submit():
    if request.method == 'POST':
        image_file = request.files["file"]
        image_file.save("static/upload/{}".format(image_file.filename))
        data = request.form
        print(image_file, data.get("username"), data.get("restaurant_name"), data.get("rating1"), data.get("rating2"), data.get("rating3"), data.get("rating4"), data.get("rating5"), data.get("rating6"), data.get("review"))

        if DB.insert_review(data, image_file.filename):
            return render_template("WriteReview_result.html", data=data, img_path="static/upload/"+image_file.filename)

    
#RegisterPage
@application.route("/submit_register",methods=['POST'])
def reg_register_submit():
    if request.method == 'POST':
        image_file=request.files["register_img"]
        image_file.save("static/upload/{}".format(image_file.filename))
        img_path="/static/upload/"+image_file.filename
        data = request.form
        if DB.insert_restaurant(data['name'], data, img_path):
            return render_template("RegisterPage_result.html", data=data, img_path=img_path)
        else:
            return "이미 등록된 식당입니다!"


#AddMenu
@application.route("/submit_menu", methods=['POST'])
def reg_menu_submit():
    if request.method == 'POST' :
        image_file=request.files["newmenuimg"]
        image_file.save("static/upload/{}". format(image_file.filename))
        img_path="/static/upload/" + image_file.filename
        data = request.form
        print(image_file, data.get("restaurant"), data.get("menuname"), data.get("menuprice"), data.get("menudesc"))

        if DB.insert_menu(data, img_path):
            return render_template("AddMenu_result.html", data=data, img_path=img_path)
        else:
            return "이미 등록된 메뉴입니다!"

#DeleteMenu
@application.route("/delete_menu", methods=['POST'])
def del_menu():
    data = request.form
    menuname = data.get("menuname")
    resname = data.get("resname")
    print(menuname)

    DB.delete_menu(menuname)
    return redirect(url_for('viewmenu', name=resname))

    
# Login	
@application.route("/submit_login", methods=['POST'])	
def reg_login_submit():	
    data = request.form	
    user_id = request.form.get("id")	
    user_pw = request.form.get("password")	
    user_pw_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()	
    	
    if DB.user_login(user_id, user_pw_hash):	
        session['UserId'] = user_id	
        session['like_restaurant'] = DB.get_like_restaurant_byuser(str(user_id))	
        #return render_template("index.html", data=data)	
        return redirect(url_for('index'))	
    elif (user_id and user_pw):	
        flash("아이디나 패스워드를 확인해주세요")	
        return render_template("Login.html")
    
# Logout
@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for('index'))

# SignUp
@application.route("/submit_signup", methods=['POST'])
def reg_signup_submit():
    ID = request.form.get("id")
    confirmcode = request.form.get("confirmcode")
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    password_hash = hashlib.sha256(password1.encode('utf8')).hexdigest()
    
    data = {"UserId" : ID,
            "UserPassword" : password_hash}
    
    if not (ID and password1 and password2) :
        flash("모두 입력해주세요")
    elif (len(password1) <6):
        flash("비밀번호는 6자 이상이어야 합니다")
    elif password1 != password2:
        flash("비밀번호를 확인해주세요")
    elif DB.insert_account(ID, data):
        flash("가입 완료되었습니다")
    else: 
        flash("이미 가입된 계정입니다")
    return render_template("SignUp.html", data=data)

# 탈퇴하기
@application.route("/delete_account")
def delete_user():
    if DB.delete_account(session['UserId']):
        session.clear()
    return redirect(url_for('index'))

#Register-Menu
@application.route("/register_menu",methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("AddMenu.html",data=data)



@application.route("/dynamicurl/<variable_name>/")
def DynamicUrl(variable_name):
    return str(variable_name)


# Index
@application.route("/index")
def index_restaurants():
    data=DB.get_restaurant().get()
    res=list()
    for datas in data.each():
        res.append(datas.val())

    name=[]
    for names in data.each():
        name.append(names.val()['name'])

    avg_rate=[]
    for names in name:
        value=DB.get_avgrate_by_name(names)
        avg_rate.append(value)

    rate_dic=dict(zip(name, avg_rate))
    
    for value in res:
        for names in rate_dic.keys():
            if names==value['name']:
                if rate_dic[names]=='':
                    value['rate']=0
                else:
                    value['rate']=rate_dic[names]

    # tot_count = len(data)
    data = sorted(res, key=lambda x: x['rate'], reverse=True)
    
    import random
    num=random.randint(0, len(data)-1)

    return render_template("index.html",datas=list(data[:3]), data=data, num=num)


# 상세 페이지 동적 라우팅
@application.route("/specificscreen/<name>/")
def view_restaurant_detail(name):
    data = DB.get_restaurant_byname(str(name))

    review = DB.get_reviews_byResName(str(name))
    avg_rate = DB.get_avgrate_by_name(str(name))

    check = DB.get_opening_days(str(name))
    print("####data:",data)
    return render_template("SpecificScreen.html", data=data, avg_rate=avg_rate, check=check)



#리뷰 페이지 동적 라우팅
@application.route("/viewreview/<name>/")
def view_reviews(name):
    name = name
    data = DB.get_reviews_byResName(str(name))   # 데이터 찾아오기
    num = len(data)
    
    avg_rating = DB.get_avgrate_by_name(str(name))
    rating1, rating2, rating3, rating4, rating5, rating6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    if num > 0:
        for i in range(num):
            rating1 += data[i]['rating1']
            rating2 += data[i]['rating2']
            rating3 += data[i]['rating3']
            rating4 += data[i]['rating4']
            rating5 += data[i]['rating5']
            rating6 += data[i]['rating6']

        rating1 = rating1 / num
        rating2 = rating2 / num
        rating3 = rating3 / num
        rating4 = rating4 / num
        rating5 = rating5 / num
        rating6 = rating6 / num
    
    rating1 = np.round(rating1, 1)
    rating2 = np.round(rating2, 1)
    rating3 = np.round(rating3, 1)
    rating4 = np.round(rating4, 1)
    rating5 = np.round(rating5, 1)
    rating6 = np.round(rating6, 1)
    
    return render_template("ViewReview.html", 
                           data = data, 
                           name = name, 
                           num = num,
                           avg_rate = avg_rating,
                           rate1 = rating1,
                           rate2 = rating2,
                           rate3 = rating3,
                           rate4 = rating4,
                           rate5 = rating5,
                           rate6 = rating6
                          )




#리뷰 작성 페이지 동적 라우팅
@application.route("/writereview/<name>/")
def write_review(name):
    name = name
    return render_template("WriteReview.html", name = name)


if __name__ == "__main__": application.run(host='0.0.0.0', debug=True)
