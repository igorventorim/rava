# encoding: utf-8

from flask import request, Blueprint
from virtual_class.virtual_class_service import VirtualClassService
from messenger.messenger_service import MessengerService
from config.configuration import Configuration
virtual_class_blueprint = Blueprint('virtual_class_blueprint', __name__)

#AÇÕES RELACIONADAS AO MÓDULO DE SALA DE AULA VIRTUAL

service_virtual_class = VirtualClassService()

@virtual_class_blueprint.route("/pnota")
def structPNota():
    r = service_virtual_class.generateStructPNota()
    # controller.writeData()
    print(r)
    return r, 200


@virtual_class_blueprint.route("/samplesimulation")
def simulation():
    service_virtual_class.sampleSimulation()
    return "ok", 200


@virtual_class_blueprint.route("/test")
def testSendMessage():
    print(request.args.get("message"))
    msg = request.args.get("message")
    MessengerService.sendMessageTest(msg)
    return "ok", 200


@virtual_class_blueprint.route('/response', methods=['POST'])
def updateAnswers():
    service_virtual_class.updateAnswers(request.get_json())
    return "ok", 200


@virtual_class_blueprint.route("/generateDB")
def generate():
    Configuration.db.create_all()
    print(Configuration.db)
    return "ok",200
