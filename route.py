# encoding: utf-8

from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

SQLAlchemy.SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from virtual_class.virtual_class_controller import virtual_class_blueprint
from messenger.messenger_controller import messenger_blueprint
from ru.ru_controller import ru_blueprint
from virtual_class.virtual_class_service import VirtualClassService

app.register_blueprint(virtual_class_blueprint)
app.register_blueprint(messenger_blueprint)
app.register_blueprint(ru_blueprint)
controller = VirtualClassService()


if __name__ == '__main__':
    app.run(debug=True)


# @app.route("/registerStartedButton")
# def registerStartedButton():
#      r = MessengerProfile().createStartedButton()
#      if(r == True):
#         return "ok", 200
#      else:
#          return "erro", 200

# @app.route("/registerMsgGreeting")
# def registerMsgGreeting():
#     r= MessengerProfile().createGreeting()
#     if (r == True):
#         return "ok", 200
#     else:
#         return "erro", 200

# @app.route("/readGreeting")
# def readGreeting():
#     r = MessengerProfile().readGreeting()
#     print(r)
#     return r["data"], 200
