
from flask import Flask 
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from myproject.database.db import initialize_db


 

app = Flask(__name__)

app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "testststst"
app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/movie-bag'
 }
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = "465"
app.config["MAIL_USERNAME"] = "moyogundare@gmail.com"
app.config["MAIL_PASSWORD"] = "eberechi"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

api = Api(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

mail = Mail(app)

#app.config['MONGO_URI'] = "mongodb+srv://lordchappy:Eberechi123@cluster0.angpe.mongodb.net/test"
initialize_db(app)

from myproject.resources.routes import initialize_routes
initialize_routes(api)
