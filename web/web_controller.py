from flask import Blueprint, render_template, request, send_from_directory

from web.web_service import WebService

web_blueprint = Blueprint('web_blueprint', __name__)

web_service = WebService()

@web_blueprint.route("/cadastrar_simulado",methods=['GET', 'POST'])
def avaliation():
    if request.method == 'POST':
        file = request.files['file']
        teacher = request.form['teacher']
        test_name = request.form['test_name']
        list = file.readlines()

        return web_service.register_simulado(list,test_name,teacher)
    else:
        return render_template('upload.html')

@web_blueprint.route("/download",methods=['GET', 'POST'])
def download():
    return send_from_directory(directory="web",filename="modelo.csv",as_attachment=True)

@web_blueprint.route("/getSimulado",methods=['GET'])
def getSimulado():
    test_name= request.args['simulado']
    return web_service.getSimulado(test_name)