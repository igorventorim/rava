# encoding: utf-8

from flask import request, Blueprint
from virtual_class.requestService import RequestService
from route import db
from route import app

controller = RequestService()

comunicador_blueprint = Blueprint('comunicador_blueprint',__name__)

@comunicador_blueprint.route("/pnota")
@app.route("/pnota")
def structPNota():
    r = controller.generateStructPNota()
    # controller.writeData()
    print(r)
    return r, 200

# @comunicador_blueprint.route("/samplesimulation")
@app.route("/samplesimulation")
def simulation():
    controller.sampleSimulation()
    return "ok", 200

# @comunicador_blueprint.route("/test")
@app.route("/test")
def testSendMessage():
    print(request.args.get("message"))
    msg = request.args.get("message")
    controller.sendMessageTest(msg)
    return "ok", 200

# @comunicador_blueprint.route('/response', methods=['POST'])
@app.route('/response', methods=['POST'])
def updateAnswers():
    controller.updateAnswers(request.get_json())
    return "ok", 200

# @comunicador_blueprint.route("/generateDB")
@app.route("/generateDB")
def generate():
    db.create_all()
    print(db)
    return "ok",200