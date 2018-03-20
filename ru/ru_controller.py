# encoding: utf-8
from ru.ru_service import RUService

from flask import Blueprint
from service.sinc_data import SincData

ru_blueprint = Blueprint('ru_blueprint', __name__)

#AÇÕES RELACIONADAS AO MÓDULO DO RUService

ru_service = RUService()
sinc = SincData()

@ru_blueprint.route("/sendMenus")
def send_menus():
    ru_service.sendMenus()
    return "ok", 200

@ru_blueprint.route("/sincMenu")
def sinc_menu():
    sinc.run()
    return "ok", 200
