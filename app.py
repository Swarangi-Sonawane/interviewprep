from flask import Flask
from routes.home import home
from routes.login import login
app=Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(login)
if __name__ == "__main__":
    app.run(debug=True)