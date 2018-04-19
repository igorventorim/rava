# encoding: utf-8
from ru.ru_service import RUService
from flask import Blueprint
from service.sinc_data import SincData
from ru.ru_db_extractor.extractor_ru_service import ExtractorRUService

ru_blueprint = Blueprint('ru_blueprint', __name__)

#AÇÕES RELACIONADAS AO MÓDULO DO RU

ru_service = RUService()
extract = ExtractorRUService()

@ru_blueprint.route("/sendMenus")
def send_menus():
    ru_service.sendMenus()
    return "ok", 200

@ru_blueprint.route("/sincMenu")
def sinc_menu():
    extract.menu()
    # extract.generateJson()
    return "ok", 200