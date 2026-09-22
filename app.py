from flask import Flask
from routes.home import home
from routes.login import login
from routes.register import register
from routes.subject import subject
from admin.admin_login import admin_login
from admin.dashboard import dashboard
app=Flask(__name__)
app.secret_key="prepmate-secret-key"
app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(subject)
app.register_blueprint(admin_login)
app.register_blueprint(dashboard)
if __name__ == "__main__":
    app.run(debug=True)