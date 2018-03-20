# encoding: utf-8
from ru.ru_service import RUService

from flask import Blueprint

ru_blueprint = Blueprint('ru_blueprint', __name__)

#AÇÕES RELACIONADAS AO MÓDULO DO RUService

ru_service = RUService()

@ru_blueprint.route("/sendMenus")
def sendMenus():
    ru_service.sendMenus()
    return "ok", 200