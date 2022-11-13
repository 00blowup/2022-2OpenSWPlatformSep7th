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

@application.route("/registerpage")
def registerpage():
    return render_template("RegisterPage.html")

@application.route("/signup")
def signup():
    return render_template("Signup.html")

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
    return render_template("WriteReview.html")

@application.route("/writereview")
def writereview():
    return render_template("WriteReview.html")

#WriteReview
@application.route("/submit_review", methods=['POST'])
def reg_review_submit():
    image_file = request.files["review_img"]
    image_file.save("static/img/review_image.png")
    data = request.form
    return render_template("WriteReview_result.html", data=data)


#AddMenu
@application.route("/submit_menu", methods=['POST'])
def reg_menu_submit():
    if request.method == 'POST' :
        data = request.form
        return render_template("AddMenu_result.html", data=data)




application.run(debug=True)



