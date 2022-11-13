from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addmenu")
def addmenu():
    return render_template("AddMenu.html")

@app.route("/bytypepage")
def bytypepage():
    return render_template("ByTypePage.html")

@app.route("/ganadapage")
def ganadapage():
    return render_template("GanadaPage.html")

@app.route("/locationtypepage")
def locationtypepage():
    return render_template("LocationTypePage.html")

@app.route("/login")
def login():
    return render_template("Login.html")

@app.route("/registerpage")
def registerpage():
    return render_template("RegisterPage.html")

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/specificscreen")
def specificscreen():
    return render_template("SpecificScreen.html")

@app.route("/typespage")
def typespage():
    return render_template("TypesPage.html")

@app.route("/viewmenu")
def viewmenu():
    return render_template("ViewMenu.html")

@app.route("/viewreview")
def viewreview():
    return render_template("WriteReview.html")

@app.route("/writereview")
def writereview():
    return render_template("WriteReview.html")


app.run(debug=True)