from flask import Flask, render_template, request, flash, redirect, url_for
from database import DBhandler

application = Flask(__name__)
application.secret_key = 'eatwha_secret'

DB = DBhandler()

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/addmenu")
def addmenu():
    return render_template("AddMenu.html")

@application.route("/bytypepage")
def bytypepage():
    return render_template("ByTypePage.html")

@application.route("/ganadapage")
def ganadapage():
    return render_template("GanadaPage.html")

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

@application.route("/viewmenu")
def viewmenu():
    return render_template("ViewMenu.html")

@application.route("/viewreview")
def viewreview():
    return render_template("ViewReview.html")

@application.route("/writereview")
def writereview():
    return render_template("WriteReview.html")

@application.route("/mypage")
def mypage():
    return render_template("MyPage.html")


#WriteReview
@application.route("/submit_review", methods=['POST'])
def reg_review_submit():
    if request.method == 'POST':
        image_file = request.files["file"]
        image_file.save("static/upload/{}".format(image_file.filename))
        data = request.form
        print(image_file, data.get("rating1"), data.get("rating2"), data.get("rating3"), data.get("rating4"), data.get("rating5"), data.get("rating6"), data.get("review"))

        if DB.insert_review(data, image_file.filename):
            return render_template("WriteReview_result.html",data=data,img_path="static/upload/"+image_file.filename)


    
    #RegisterPage
@application.route("/submit_register",methods=['POST'])
def reg_register_submit():
    image_file=request.files["register_img"]
    image_file.save("static/upload/{}".format(image_file.filename))
    data = request.form
    rest_name=request.form.get("name")
    if DB.insert_restaurant(rest_name,data, image_file.filename):
        return render_template("RegisterPage_result.html", data=data, img_path="static/upload/" + image_file.filename)
    else:
        return "이미 등록된 식당입니다!"


#AddMenu
@application.route("/submit_menu", methods=['POST'])
def reg_menu_submit():
    if request.method == 'POST' :
        image_file=request.files["newmenuimg"]
        image_file.save("static/upload/{}". format(image_file.filename))
        data = request.form
        print(image_file, data.get("restaurant"), data.get("menuname"), data.get("menuprice"), data.get("menudesc"))

        if DB.insert_menu(data, image_file.filename):
            return render_template("AddMenu_result.html", data=data, img_path="static/upload/" + image_file.filename)
        else:
            return "이미 등록된 메뉴입니다!"
    
# Login
@application.route("/submit_login", methods=['POST'])
def reg_login_submit():
    data = request.form
    user_id = request.form.get("id")
    user_pw = request.form.get("password")
    print(data.get("id"), data.get("password"))
    if DB.user_login(user_id, user_pw):
        return render_template("index.html", data=data)
    elif (user_id and user_pw):
        return render_template("Login.html", data=data)

# SignUp
@application.route("/submit_signup", methods=['POST'])
def reg_signup_submit():
    ID = request.form.get("id")
    confirmcode = request.form.get("confirmcode")
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    data = {"UserId" : ID,
            "UserPassword" : password1}
    print(data.get("UserId"), data.get("UserPassword"))
    
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


#Register-Menu
@application.route("/register_menu",methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("AddMenu.html",data=data)

#Show ganadalistPage
@application.route("/ganadalist")
def ganadalist_restaurants():
    data = DB.get_restaurants()

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
        elif('나'<=(name[x][0]) and (name[x][0])<'다'):
            na_name.append(name[x])
        x+=1
    print(ga_name)
    
    return render_template("GanadaPage.html", ga_data=ga_name, na_data=na_name)

if __name__ == "__main__": application.run(host='0.0.0.0', debug=True)



