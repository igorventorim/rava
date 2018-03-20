# encoding: utf-8

from flask import Flask
from config.configuration import Configuration
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

SQLAlchemy.SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sched = BackgroundScheduler()
Configuration.db = db

from service.sinc_data import SincData
from virtual_class.virtual_class_controller import virtual_class_blueprint
from messenger.messenger_controller import messenger_blueprint
from ru.ru_controller import ru_blueprint

app.register_blueprint(virtual_class_blueprint)
app.register_blueprint(messenger_blueprint)
app.register_blueprint(ru_blueprint)
sinc = SincData()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    sinc.run()
    print("FUNCIONOU!!!")

if __name__ == '__main__':
    sched.start()
    # sinc.run()
    app.run(debug=True)

