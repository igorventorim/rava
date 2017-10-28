from flask import Flask, request,render_template, redirect, url_for, session,flash
import os

app = Flask(__name__)


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
    request.get_json()
    return "ok", 200


@app.route("/home")
def home():
    return "<h1>Hello World</hi>"


if __name__ == '__main__':
    app.run(debug=True)

