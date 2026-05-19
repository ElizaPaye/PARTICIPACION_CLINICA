from database import db


class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.Text, nullable=False)
    tratamiento = db.Column(db.Text, nullable=False)

    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)

    # Relaciones
    medico = db.relationship('Medico', backref='consultas')
    paciente = db.relationship('Paciente', backref='consultas')

    def __init__(self, medico_id, paciente_id, diagnostico, tratamiento, fecha):
        self.medico_id = medico_id
        self.paciente_id = paciente_id
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.fecha = fecha

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Consulta.query.all()

    @staticmethod
    def get_by_id(id):
        return Consulta.query.get(id)

    def update(self, medico_id=None, paciente_id=None, diagnostico=None, tratamiento=None, fecha=None):
        if medico_id and paciente_id and diagnostico and tratamiento and fecha:
            self.medico_id = medico_id
            self.paciente_id = paciente_id
            self.diagnostico = diagnostico
            self.tratamiento = tratamiento
            self.fecha = fecha

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()