from flask import Flask, render_template, request

application = Flask(__name__)

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


#WriteReview
@application.route("/submit_review", methods=['POST'])
def reg_review_submit():
    image_file = request.files["review_img"]
    image_file.save("static/uploads/review_image.png")
    data = request.form
    rating = data.get("rating")
    review = data.get("review")
    print(image_file, rating, review)
    return render_template("WriteReview_result.html", data=data)


#RegisterPage
@application.route("/submit_register",methods=['POST'])
def reg_register_submit():
    image_file=request.files["file"]
    image_file.save("static/uploads/register_image.png")
    data = request.form
    print(image_file, data.get("name"), data.get("type"), data.get("location"), data.get("locationdetail"), data.get("phone"), data.get("day"), data.get("start"), data.get("end"), data.get("bstart"), data.get("bend"), data.get("extra"))
    return render_template("RegisterPage_result.html",data=data)


#AddMenu
@application.route("/submit_menu", methods=['POST'])
def reg_menu_submit():
    if request.method == 'POST' :
        image_file=request.files["newmenuimg"]
        image_file.save("static/uploads/menu_image.png")
        data = request.form
        print(image_file, data.get("menuname"), data.get("menuprice"), data.get("menudesc"))
        return render_template("AddMenu_result.html", data=data)
    
# Login
@application.route("/submit_login", methods=['POST'])
def reg_login_submit():
    data = request.form
    print(data.get("id"), data.get("password"))
    return render_template("Login_result.html", data=data)

# SignUp
@application.route("/submit_signup", methods=['POST'])
def reg_signup_submit():
    data = request.form
    print(data.get("id"), data.get("password1"), data.get("password2"))
    return render_template("SignUp_result.html", data=data)

application.run(debug=True)



