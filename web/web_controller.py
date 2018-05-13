from flask import Blueprint, render_template, request, send_from_directory

web_blueprint = Blueprint('web_blueprint', __name__)


@web_blueprint.route("/cadastrar_simulado",methods=['GET', 'POST'])
def avaliation():
    if request.method == 'POST':
        file = request.files['file']
        print(file.readlines())
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')

@web_blueprint.route("/download",methods=['GET', 'POST'])
def download():
    return send_from_directory(directory="web",filename="modelo.csv",as_attachment=True)