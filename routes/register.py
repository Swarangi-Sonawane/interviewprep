from flask import Blueprint,render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from database import get_connection

register=Blueprint("register",__name__)

@register.route("/register",methods=["get","post"])
def register_page():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        confirm_password=request.form["confirm_password"]
        if password!=confirm_password:
            flash("password do not match")
        else:
            hashed_password=generate_password_hash(password)
            connection=get_connection()
            cursor=connection.cursor()
            cursor.execute("insert into users(name,email,password) values (%s,%s,%s)",(name,email,hashed_password))
            connection.commit()
            cursor.close()
            connection.close()
            flash("Registration Successful! Please Login.")
            return redirect(url_for("login.login_page"))
    return render_template("register.html")