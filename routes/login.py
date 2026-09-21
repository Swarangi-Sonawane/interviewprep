from flask import Blueprint, render_template,request,url_for,redirect,flash 
from database import get_connection
from werkzeug.security import check_password_hash
login=Blueprint("login",__name__)
@login.route("/login",methods=["GET","POST"])
def login_page():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("select uid,name,password from users where email=%s",(email,))
        user=cursor.fetchone()
        if user is not None:
            stored_password=user[2]
            if check_password_hash(stored_password,password):
                return redirect(url_for("subject.subject_page"))
            else:
                flash("Invalid email or password")
        else:
            flash("Invalid email or password")
        cursor.close()
        connection.close()
    return render_template("login.html")