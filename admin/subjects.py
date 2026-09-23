from flask import Blueprint,render_template,request,redirect,url_for
from database import get_connection
subjects=Blueprint("subjects",__name__)
@subjects.route("/admin/subjects",methods=["GET","POST"])
def subjects_page():
    if request.method=="POST":
        s_name=request.form["s_name"]
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("insert into subjects (s_name) values (%s)",(s_name,))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for("subjects.subjects_page"))
    
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("select sid,s_name from subjects order by sid")
    subject_list=cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("admin/subjects.html",subjects=subject_list)
@subjects.route("/admin/subjects/edit", methods=["POST"])

def edit_subject():
    sid = request.form["sid"]
    s_name = request.form["s_name"]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("update subjects SET s_name = %s where sid = %s",(s_name, sid))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("subjects.subjects_page"))

@subjects.route("/admin/subjects/delete", methods=["POST"])
def delete_subject():
    sid = request.form["sid"]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("delete from subjects WHERE sid = %s", (sid,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("subjects.subjects_page"))
