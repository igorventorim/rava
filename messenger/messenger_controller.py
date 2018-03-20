# encoding: utf-8

from flask import request, Blueprint
from config.configuration import Configuration
from messenger.messenger_profile import MessengerProfile
from messenger.messenger_service import MessengerService


messenger_blueprint = Blueprint('messenger_blueprint',__name__)

#AÇÕES RELACIONADAS A CONFIGURAÇÃO E FUNCIONAMENTO DO MESSENGER.

messenger_service = MessengerService()

@messenger_blueprint.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Configuration.VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return home()


@messenger_blueprint.route('/', methods=['POST'])
def webhook():

    messenger_service.unpackMessage(request.get_json())
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
