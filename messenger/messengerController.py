# encoding: utf-8

from flask import Flask, request, Blueprint
from config.authentication import Authentication
from virtual_class.requestService import RequestService
from messenger.messengerProfile import MessengerProfile

controller = RequestService()

messenger_blueprint = Blueprint('messenger_page',__name__)

@messenger_blueprint.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Authentication.VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return home()

@messenger_blueprint.route('/', methods=['POST'])
def webhook():
    controller.unpackMessage(request.get_json())
    return "ok", 200

@messenger_blueprint.route("/home")
def home():
    return "<h1>Robo de Auxilio Virtual ao Aprendizado!</hi>"

@messenger_blueprint.route("/registerStartedButton")
def registerStartedButton():
     r = MessengerProfile().createStartedButton()
     if(r == True):
        return "ok", 200
     else:
        return "erro", 200

@messenger_blueprint.route("/registerMsgGreeting")
def registerMsgGreeting():
    r= MessengerProfile().createGreeting()
    if (r == True):
        return "ok", 200
    else:
        return "erro", 200

@messenger_blueprint.route("/readGreeting")
def readGreeting():
    r = MessengerProfile().readGreeting()
    print(r)
    return r["data"], 200
