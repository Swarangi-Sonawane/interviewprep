from flask import Blueprint,render_template
from database import get_connection
dashboard=Blueprint("dashboard",__name__)
@dashboard.route("/admin/dashboard")
def dashboard_page():
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("select count(*) from users")
    total_students=cursor.fetchone()[0]

    cursor.execute("select count(*) from subjects")
    total_subjects=cursor.fetchone()[0]

    cursor.execute("select count(*) from admins")
    total_admins=cursor.fetchone()[0]

    cursor.close()
    connection.close()
    return render_template("admin/dashboard.html",total_students=total_students,total_subjects=total_subjects,total_admins=total_admins)