# encoding: utf-8

from flask import Flask, request,render_template, redirect, url_for, session,flash
import os
from flask_sqlalchemy import SQLAlchemy

from authentication import Authentication
from messengerProfile import MessengerProfile

SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from requestController import RequestController
controller =  RequestController()

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Authentication.VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return home()

@app.route('/', methods=['POST']) 
def webhook():
    controller.unpackMessage(request.get_json())
    return "ok", 200


@app.route("/home")
def home():
    return "<h1>Robo de Auxilio Virtual ao Aprendizado!</hi>"

@app.route("/registerStartedButton")
def registerStartedButton():
     r = MessengerProfile().createStartedButton()
     if(r == True):
        return "ok", 200
     else:
         return "erro", 200

@app.route("/registerMsgGreeting")
def registerMsgGreeting():
    r= MessengerProfile().createGreeting()
    if (r == True):
        return "ok", 200
    else:
        return "erro", 200

@app.route("/readGreeting")
def readGreeting():
    r = MessengerProfile().readGreeting()
    print(r)
    return r["data"], 200

@app.route("/pnota")
def structPNota():
    r = controller.generateStructPNota()
    controller.writeData()
    print(r)
    return r, 200

@app.route("/samplesimulation")
def simulation():
    controller.sampleSimulation()
    return "ok", 200

@app.route("/test")
def testSendMessage():
    print(request.args.get("message"))
    msg = request.args.get("message")
    controller.sendMessageTest(msg)
    return "ok", 200


@app.route("/generateDB")
def generate():
    db.create_all()
    return "ok",200

if __name__ == '__main__':
    app.run(debug=True)

