# encoding: utf-8

from flask import request
from virtual_class.requestService import RequestService

controller = RequestService()

@app.route("/pnota")
def structPNota():
    r = controller.generateStructPNota()
    # controller.writeData()
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

@app.route('/response', methods=['POST'])
def updateAnswers():
    controller.updateAnswers(request.get_json())
    return "ok", 200