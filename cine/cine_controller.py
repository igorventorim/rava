# encoding: utf-8

from flask import request, Blueprint
from cine.sinc_cine_data import SincCineData

cine_blueprint = Blueprint('cine_blueprint',__name__)

@cine_blueprint.route("/sincMoviesWeek")
def sincCine():
    sinc = SincCineData()
    sinc.extract_data_cine()
    return "ok"