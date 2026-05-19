from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # admin / medico
    fecha_reg = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, password, rol):
        self.username = username
        self.password = generate_password_hash(password)
        self.rol = rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return Usuario.query.all()

    def check_password(self, password):
        return check_password_hash(self.password, password)