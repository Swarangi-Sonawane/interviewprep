from flask import Blueprint,render_template,redirect,url_for,session
home=Blueprint("home",__name__)
@home.route("/")
def home_page():
    return render_template("home.html")