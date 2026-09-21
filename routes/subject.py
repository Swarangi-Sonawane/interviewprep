from flask import Blueprint,render_template
subject=Blueprint("subject",__name__)
@subject.route("/subject")
def subject_page():
    return render_template("subject.html")