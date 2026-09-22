from flask import Blueprint,render_template
dashboard=Blueprint("dashboard",__name__)
@dashboard.route("/admin/dashboard")
def dashboard_page():
    return render_template("admin/dashboard.html")