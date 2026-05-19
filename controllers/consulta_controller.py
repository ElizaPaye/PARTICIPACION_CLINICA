from flask import request, redirect, url_for, Blueprint
from datetime import datetime

from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente

from views import consulta_view

consulta_bp = Blueprint('consulta', __name__, url_prefix="/consultas")


@consulta_bp.route("/")
def index():
    consultas = Consulta.get_all()
    return consulta_view.list(consultas)


@consulta_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        fecha_str = request.form['fecha']

        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        consulta = Consulta(
            medico_id=medico_id,
            paciente_id=paciente_id,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            fecha=fecha
        )

        consulta.save()
        return redirect(url_for('consulta.index'))

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return consulta_view.create(medicos, pacientes)


@consulta_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    consulta = Consulta.get_by_id(id)

    if request.method == 'POST':
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        fecha_str = request.form['fecha']

        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        consulta.update(
            medico_id=medico_id,
            paciente_id=paciente_id,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            fecha=fecha
        )

        return redirect(url_for('consulta.index'))

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return consulta_view.edit(consulta, medicos, pacientes)


@consulta_bp.route("/delete/<int:id>")
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()

    return redirect(url_for('consulta.index'))