# encoding: utf-8

from flask import Flask
from config.configuration import Configuration
from flask_sqlalchemy import SQLAlchemy

from utils.redis import Redis

SQLAlchemy.SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__,template_folder="web/views",static_folder="web")
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Configuration.db = db

if Configuration.REDIS_URL != None:
    Configuration.redis = Redis(Configuration.REDIS_URL)

from virtual_class.virtual_class_controller import virtual_class_blueprint
from messenger.messenger_controller import messenger_blueprint
from ru.ru_controller import ru_blueprint
from cine.cine_controller import cine_blueprint
from web.web_controller import web_blueprint

app.register_blueprint(virtual_class_blueprint)
app.register_blueprint(messenger_blueprint)
app.register_blueprint(ru_blueprint)
app.register_blueprint(cine_blueprint)
app.register_blueprint(web_blueprint)

if __name__ == '__main__':
    app.run(debug=True)