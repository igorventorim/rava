# encoding: utf-8
from flask import Flask, request,render_template, redirect, url_for, session,flash
import requests
import sys
import os
import json

app = Flask(__name__)


__PARAMS = {"access_token":  os.environ["PAGE_ACCESS_TOKEN"] }
__HEADERS = {"Content-Type": "application/json"}


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return home()

@app.route('/', methods=['POST']) 
def webhook():
    getMessage(request.get_json())
    return "ok", 200


@app.route("/home")
def home():
    return "<h1>Robo de Auxilio Virtual ao Aprendizado!</hi>"



def getMessage(data):
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                client_id = messaging_event["sender"]["id"]
                __messaging_event = messaging_event
                isMessage = "message" in __messaging_event
                isPostback = "postback" in __messaging_event
                content_message = __getPayloadOrText(isMessage,isPostback,__messaging_event)

                data_package = getResponse(client_id,content_message)
                sendMessage(data_package)



def sendMessage(data):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=__PARAMS, headers=__HEADERS, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)


def __getPayloadOrText(isMessage,isPostback,m): # just to instanciate the above
    if isMessage:
        return getMessageText(m)
    elif isPostback:
        return getPostbackPayload(m)
    else:
        raise TypeError("Message sent from client was not a text neither a payload.")


def getMessageText(messaging_event):
    if "attachments" in messaging_event["message"]:
        return "attachments" # caso o usuario clicar no joinha da isso
    else:
        return messaging_event["message"]["text"]

def getPostbackPayload(messaging_event):
    return messaging_event["postback"]["payload"]


def getResponse(client_id,text):
    return json.dumps({
                        "recipient": {
                            "id": client_id
                        },
                        "message": {
                            "text": text
                        }
                          })



if __name__ == '__main__':
    app.run(debug=True)

