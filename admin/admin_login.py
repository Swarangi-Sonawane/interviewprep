from flask import Blueprint,render_template,request,redirect,url_for,flash
from werkzeug.security import check_password_hash
from database import get_connection
admin_login=Blueprint("admin_login",__name__)
@admin_login.route("/admin/login", methods=["GET","POST"])
def admin_login_page():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("select password from admins where email=%s",(email,))
        admin=cursor.fetchone()
        cursor.close()
        if admin is not None:
            stored_password=admin[0]
            if check_password_hash(stored_password,password):
                return redirect(url_for("dashboard.dashboard_page"))
        flash("Invalid email or password")
    return render_template("admin/admin_login.html")