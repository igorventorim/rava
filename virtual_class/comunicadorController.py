# encoding: utf-8

from flask import request, Blueprint
from route import db
from virtual_class.requestService import RequestService
from route import app



# comunicador_blueprint = Blueprint('comunicador_blueprint',__name__)
controller = RequestService()

@app.route("/pnota")
# @comunicador_blueprint.route("/pnota")
def structPNota():
    r = controller.generateStructPNota()
    # controller.writeData()
    print(r)
    return r, 200

@app.route("/samplesimulation")
# @comunicador_blueprint.route("/samplesimulation")
def simulation():
    controller.sampleSimulation()
    return "ok", 200

@app.route("/test")
# @comunicador_blueprint.route("/test")
def testSendMessage():
    print(request.args.get("message"))
    msg = request.args.get("message")
    controller.sendMessageTest(msg)
    return "ok", 200

@app.route('/response', methods=['POST'])
# @comunicador_blueprint.route('/response', methods=['POST'])
def updateAnswers():
    controller.updateAnswers(request.get_json())
    return "ok", 200

@app.route("/generateDB")
# @comunicador_blueprint.route("/generateDB")
def generate():
    db.create_all()
    print(db)
    return "ok",200